"""Focused check: Does Bandra have workers with active policies?"""
from config import get_settings
from db.models import get_engine, get_session_factory, Worker, Policy, PolicyStatusEnum

settings = get_settings()
engine = get_engine(settings.database_url)
SessionLocal = get_session_factory(engine)

with SessionLocal() as session:
    eligible = (
        session.query(Worker)
        .join(Policy, Policy.worker_id == Worker.id)
        .filter(
            Worker.zone_id == "zone-bandra",
            Worker.is_active == True,
            Policy.status == PolicyStatusEnum.active,
        )
        .all()
    )
    
    with open("debug_eligible.txt", "w") as f:
        f.write(f"Eligible workers in zone-bandra: {len(eligible)}\n")
        for w in eligible:
            f.write(f"  {w.id} ({w.name})\n")
        
        # Also check: worker-salim specifically
        salim = session.get(Worker, "worker-salim")
        if salim:
            f.write(f"\nSalim: zone={salim.zone_id}, active={salim.is_active}\n")
            policy = session.query(Policy).filter(
                Policy.worker_id == "worker-salim",
                Policy.status == PolicyStatusEnum.active
            ).first()
            if policy:
                f.write(f"Policy: status={policy.status}, cap={policy.coverage_cap_rs}, paid={policy.amount_paid_rs}\n")
            else:
                f.write("NO ACTIVE POLICY\n")
        else:
            # Check if any worker with ID containing 'salim' exists
            all_workers = session.query(Worker).all()
            f.write(f"\nAll worker IDs: {[w.id for w in all_workers]}\n")

print("Done")
