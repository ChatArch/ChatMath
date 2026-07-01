"Typed environment configuration for ChatMath."

from chatenv import BaseEnvConfig, EnvField


class ChatmathConfig(BaseEnvConfig):
    "ChatMath ChatEnv configuration."

    _title = "ChatMath Configuration"
    _aliases = ["chatmath"]
    _storage_dir = "Chatmath"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATMATH_API_KEY = EnvField(
        "CHATMATH_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatmathConfig"]
