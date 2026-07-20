import time

class AgentKeyLiveDataGatewayClient:
    SOURCES = {
        "search":   [{"title": "AI agents hit $50B market cap", "url": "https://techcrunch.com/ai-agents"},
                     {"title": "Top 10 agentic frameworks 2026", "url": "https://devhunt.io/agentic"}],
        "finance":  [{"ticker": "NVDA", "price": 142.87, "volume": "45M"},
                     {"ticker": "MSFT", "price": 498.23, "volume": "22M"}],
        "crypto":   [{"coin": "BTC", "price": 98542.10, "change_24h": "+2.3%"},
                     {"coin": "ETH", "price": 3821.45, "change_24h": "-0.8%"}],
        "ecommerce":[{"product": "MacBook Pro M4", "avg_price": 2499, "trend": "stable"},
                     {"product": "DJI Drone Air 4", "avg_price": 899, "trend": "rising"}],
        "social":   [{"platform": "X", "trending": "#AIAgents", "mentions": 84200},
                     {"platform": "LinkedIn", "trending": "Agentic AI", "mentions": 31500}]
    }

    def fetch(self, data_type: str, query: str) -> dict:
        t0 = time.time()
        records = self.SOURCES.get(data_type.lower(), self.SOURCES["search"])
        filtered = [r for r in records if any(query.lower() in str(v).lower() for v in r.values())] or records
        return {
            "results": filtered,
            "source": f"AgentKey/{data_type.upper()} Gateway",
            "latency_ms": int((time.time() - t0) * 1000)
        }
