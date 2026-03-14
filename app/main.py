import argparse
import json
import subprocess 
from typing import Any, Callable, get_type_hints
import os
import sys

from openai import OpenAI

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    # Conversation memory
    messages = [{"role": "user", "content": args.p}]

    while True:

        # Ask the LLM
        chat = client.chat.completions.create(
            model="anthropic/claude-haiku-4.5",
            messages=messages,
            tools=[

                # READ TOOL
                {
                    "type": "function",
                    "function": {
                        "name": "Read",
                        "description": "Read and return the contents of a file",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "file_path": {
                                    "type": "string",
                                    "description": "The path to the file to read",
                                }
                            },
                            "required": ["file_path"],
                        },
                    },
                },

                # WRITE TOOL (NEW)
                {
                    "type": "function",
                    "function": {
                        "name": "Write",
                        "description": "Write content to a file",
                        "parameters": {
                            "type": "object",
                            "required": ["file_path", "content"],
                            "properties": {
                                "file_path": {
                                    "type": "string",
                                    "description": "The path of the file to write to"
                                },
                                "content": {
                                    "type": "string",
                                    "description": "The content to write to the file"
                                }
                            },
                        },
                    },
                },
		#BASH TOOL
		{
 			"type": "function",
 			"function": {
   				"name": "Bash",
   				"description": "Execute a shell command",
   				"parameters": {
     					"type": "object",
     					"required": ["command"],
     					"properties": {
      						 "command": {
         					 "type": "string",
        					 "description": "The command to execute"
       						},
     					},
   				},
 			},
		}

            ],
        )

        if not chat.choices or len(chat.choices) == 0:
            raise RuntimeError("no choices in response")

        message = chat.choices[0].message

        # Save assistant response
        messages.append(message)

        print("Logs from your program will appear here!", file=sys.stderr)

        # If LLM wants to use a tool
        if message.tool_calls:

            tool_call = message.tool_calls[0]
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            # -------------------
            # READ TOOL EXECUTION
            # -------------------
            if function_name == "Read":

                file_path = arguments["file_path"]

                with open(file_path, "r") as f:
                    content = f.read()

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": content
                })

            # -------------------
            # WRITE TOOL EXECUTION
            # -------------------
            elif function_name == "Write":

                file_path = arguments["file_path"]
                content = arguments["content"]

                with open(file_path, "w") as f:
                    f.write(content)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": f"Successfully wrote to {file_path}"
                })
		
	    elif function_name == "Bash":
   	        command = arguments["command"]

  

    		result = subprocess.run(
        		command,
        		shell=True,
        		capture_output=True,
        		text=True
    		)

    		output = result.stdout if result.stdout else result.stderr

   		 messages.append({
        		"role": "tool",
        		"tool_call_id": tool_call.id,
        		"content": output
    		})

        else:
            # Final answer from AI
            print(message.content)
            break




if __name__ == "__main__":
    main()
