import asyncio
import json
import openai
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

# ✅ Use Groq API
openai.api_base = "https://api.groq.com/openai/v1"
openai.api_key = "gsk_nZqsB"  # 👈 Replace this with your actual Groq API key

# MCP server endpoint
MCP_URL = "http://127.0.0.1:8000/mcp"

async def main():
    transport = StreamableHttpTransport(url=MCP_URL)
    client = Client(transport=transport)

    async with client:
        tools = await client.list_tools()
        print("🧰 Available tools:", [t.name for t in tools])

        while True:
            prompt = input("\n🧠 Enter prompt ('exit' to quit): ")
            if prompt.strip().lower() in ("exit", "quit"):
                break

            try:
                response = openai.ChatCompletion.create(
                    model="llama3-70b-8192",  # ✅ Groq-hosted LLaMA 3 model
                    messages=[{"role": "user", "content": prompt}],
                    functions=[
                        {
                            "name": t.name,
                            "description": t.description,
                            "parameters": t.inputSchema,
                        }
                        for t in tools
                    ],
                    function_call="auto"
                )

                msg = response["choices"][0]["message"]

                if msg.get("function_call"):
                    func = msg["function_call"]["name"]
                    args = json.loads(msg["function_call"]["arguments"])
                    print(f"🔧 Groq LLaMA chose tool: {func} with args {args}")

                    result = await client.call_tool(func, args)
                    print("✅ Tool result:", result.content)
                else:
                    print("🤖 LLM response:", msg["content"])

            except Exception as e:
                print("❌ Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
