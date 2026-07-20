from client import AgentKeyLiveDataGatewayClient
client = AgentKeyLiveDataGatewayClient()
result = client.fetch(data_type="finance", query="NVDA")
print(f"Source: {result['source']} | Latency: {result['latency_ms']}ms")
for r in result["results"]:
    print(f"  {r}")
