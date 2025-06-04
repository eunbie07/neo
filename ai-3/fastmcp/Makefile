.PHONY: run clear install

MCP_PORT=6274
PROXY_PORT=6277

run:
	echo 'Starting FastMCP Server...'
	@FastMCP_TIMEOUT=300000 npx @modelcontextprotocol/inspector fastmcp run main.py

stop:
	@echo "Cleaning up running Server..."
	@-lsof -ti:$(MCP_PORT), $(PROXY_PORT) | xargs kill -9 2>/dev/null || true
	@echo "Ports $(MCP_PORT) and $(PROXY_PORT) have been cleaned"

# 의존성 설치
install:
	@echo "Installing dependencies..."
	@pip install openai
	@npm install -g @modelcontextprotocol/inspector

# 서버 재시작
restart: stop run

# 도움말
help:
	@echo "Available commands:"
	@echo " make run - Start the FastMCP Server"
	@echo " make stop - Stop the FastMCP Server"
	@echo " make install - Install dependencies"
	@echo " make restart - Restart the FastMCP Server"
	@echo " make help - Show this help message"