# OpenClaw MCP setup for Weavz app integrations

<!-- weavz:discovery:start -->

Use Slack, Gmail, GitHub and Notion from OpenClaw through the hosted Weavz Model Context Protocol (MCP) connector. Sign in with OAuth, select your workspace, and connect the apps you want the client to use. The hosted connector uses Code Mode MCP.

Apps become available after they are connected for the selected Weavz user and workspace:

- [Slack MCP app access](https://weavz.io/integrations/slack)
- [Gmail MCP app access](https://weavz.io/integrations/gmail)
- [GitHub MCP app access](https://weavz.io/integrations/github)
- [Notion MCP app access](https://weavz.io/integrations/notion)

Follow the client OAuth instructions below, then discover the available tools and aliases before asking the agent to act.

[MCP app and framework directory](https://github.com/weavz/mcp-examples/blob/main/docs/integrations.md) · [All examples](https://github.com/weavz/mcp-examples) · [Weavz MCP guide](https://weavz.io/docs/guides/agent-framework-examples)

<!-- weavz:discovery:end -->

Connect an AI coding client to the apps authorized in one Weavz workspace through remote MCP. This example keeps client MCP configuration separate from the model provider and from project instructions.

## Requirements

- A current OpenClaw CLI with remote Streamable HTTP MCP support.
- A reachable Weavz platform endpoint and a Weavz account.
- A model/provider configured for the named OpenClaw profile. It has separate config and auth state, so it will not inherit the default profile's model credentials/settings. Weavz OAuth does not configure or pay for model access.

See the official [OpenClaw MCP guide](https://docs.openclaw.ai/tools/mcp) for supported transports and options.

## Setup

OpenClaw stores MCP servers in Gateway config, not project config. A named `--profile` creates separate config and state under `~/.openclaw-weavz-example`; its workspace can point at this checkout. `AGENTS.md` provides workspace instructions but does not configure MCP.

```sh
# Isolated profile; do not omit --profile for these commands.
openclaw --profile weavz-example agents add weavz-example --workspace "$PWD" --non-interactive
openclaw --profile weavz-example mcp add weavz --url https://platform.weavz.io/mcp/weavz --transport streamable-http
openclaw --profile weavz-example mcp login weavz
openclaw --profile weavz-example mcp doctor weavz --probe
```

Complete the browser sign-in, select the intended workspace, and approve the connector. The OAuth flow stores credentials in the client's own credential store. Do not add an `Authorization` header or paste a Weavz access token for the hosted personal connector.

For self-hosted Weavz, replace `https://platform.weavz.io/mcp/weavz` with `https://<your-public-weavz-host>/mcp/weavz`. The server must be reachable over HTTPS from the client.

## Verify

```sh
openclaw --profile weavz-example mcp doctor weavz --probe
openclaw --profile weavz-example agent --agent weavz-example --local --message "Use a Weavz read/search tool to confirm access. Do not modify anything." --json
```

`openclaw mcp doctor weavz --probe` probes this named server. The model-mediated prompt is a separate check: count it as passed only if the transcript shows a Weavz tool call and result. Review tool arguments and output. Do not infer live auth or a successful app action from configuration files alone.

## Project instructions

This repo includes `AGENTS.md` guidance. It does not install or configure MCP. See the client-native instruction file for rules loaded into the agent.

## Local checks

Run the dependency-free static contract checks:

```sh
python3 -m unittest discover -s tests -v
```

These check the checked-in client config and instruction/setup contract only; they make no network calls and do not prove OAuth or tool execution.

## Credentials and safety

- Keep OAuth in the client credential store. No Weavz API key, MCP access token, connected-app secret, or model key belongs in this repo.
- The endpoint scopes the connector to the workspace selected during Weavz sign-in. To change workspaces, disconnect and reauthorize.
- Tool availability follows that workspace's configuration and permissions. This example does not promise MCP App UI support.
- Before writing, sending, publishing, deleting, or changing external data, inspect the proposed action and obtain user approval.

## License

MIT. See [LICENSE](LICENSE).
