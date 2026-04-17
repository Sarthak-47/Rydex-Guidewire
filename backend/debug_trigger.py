"""Quick debug script to trace the exact crash in fire_demo_trigger."""
import traceback

from config import get_settings
from services.trigger_monitor import fire_demo_trigger

settings = get_settings()

with open("debug_result.txt", "w", encoding="utf-8") as f:
    f.write(f"DB URL: {settings.database_url}\n")
    f.write(f"Demo mode: {settings.demo_mode}\n\n")

    try:
        result = fire_demo_trigger(
            zone_id="zone-bandra",
            trigger_type="rainfall",
            database_url=settings.database_url,
            duration_minutes=90,
        )
        f.write(f"SUCCESS: {result}\n")
    except Exception as e:
        f.write(f"FAILED: {type(e).__name__}: {e}\n\n")
        f.write(traceback.format_exc())

print("Done - check debug_result.txt")
