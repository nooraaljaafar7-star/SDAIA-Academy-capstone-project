from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor

def setup_tracing():
    """Register Arize Phoenix tracer for local LLM monitoring."""
    tracer_provider = register(
        project_name="contract-audit-pipeline",
        endpoint="[http://127.0.0.1:6006/v1/traces](http://127.0.0.1:6006/v1/traces)"
    )
    LangChainInstrumentor().instrument(tracer_provider=tracer_provider)
    print("🚀 Arize Phoenix Tracing initialized successfully!")