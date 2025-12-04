import asyncio
import json
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

print("Loading the environment variables")
load_dotenv()

print("client initialisation started")
SERVERS={
    "Arithmatic": {
        "command": "uv",
        "args": [
            "run",
            "--with",
            "fastmcp",
            "fastmcp",
            "run",
            "calculator.py"
        ],
        "env": {},
        "transport": "stdio"
    },
    
    "Weather_api": {
        "command": "uv",
        "args": [
            "run",
            "weather.py"
                ],
        "env": {"WEATHER_API_KEY": "9231e0f177bb4b7582445552250511"},
        "transport": "stdio"
        },
   
   "Currency": {
    "command": "uv",
    "args": ["run", "currency_converter.py"],
    "transport": "stdio"
}
}

print("main function definition")
async def main():
    print("Inside the main function")
    client = MultiServerMCPClient(SERVERS)
    tools=await client.get_tools()
    # response=llm.invoke(user_query)
    tool_names={}
    for tool in tools:
        tool_names[tool.name]=tool
    print("tools loaded and their names :",tool_names.keys())

    llm=ChatGroq(model="llama-3.1-8b-instant")
    
    llm_with_tools=llm.bind_tools(tools)
    print("Chat started ")
    while(True):

        user_query=input("Ask Query :")
        if user_query in ['exit','quit']:
            print("I hope you enjoyed the chat ")
            break
        prompt = f"""
        You are a smart assistant. You understand user query and respond accordinlgy.
        basis on user context you know if the tool is required or not.

        Your  allowed tools are: 
        ['arithmatic_calci', 'get_current_weather', 'get_forecast', 
        'compare_weather','convert_currency']

        When no tool is needed:
        - Respond normally.
        When a tool is needed:
        - Respond using the correct structured tool call.
    
        User query: "{user_query}"

        """
    
        response=await llm_with_tools.ainvoke(prompt)

        print("first reponse generated")
       
        if not response.tool_calls:
            print("\nLLM Reply:", response.content)
            print("DEBUG: No tool calls detected.")
            continue
        else:
            print("DEBUG: Tool Calls:", response.tool_calls)

        tool_messages=[]
        for tc in response.tool_calls:
            selected_tool=tc["name"]
            selected_tool_args=tc.get("args") or {}
            selected_tool_id=tc['id']

            result=await tool_names[selected_tool].ainvoke(selected_tool_args)
            tool_messages.append(ToolMessage(tool_call_id=selected_tool_id,content=json.dumps(result)))

        final_response=await llm_with_tools.ainvoke([user_query,response,*tool_messages])
        
        print(f"final Response with tool {selected_tool}:{final_response.content}")
        

if __name__ == "__main__":
    asyncio.run(main())
    