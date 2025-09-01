from backend.main import SessionLocal, User, DocumentRecord, FormRecord, Synonym, UPLOAD_DIR, FILLED_DIR
from pathlib import Path
import shutil, json
db = SessionLocal()
def seed_user():
    u = db.query(User).filter(User.email=="ravi.kumar@example.com").first()
    if u:
        print("User already exists")
        return u
    u = User(email="ravi.kumar@example.com", password_hash="$2b$12$abcdefghijklmnopqrstuv", name="Ravi Kumar", dob="2002-05-21", phone="9876543210", address="123, MG Road, Pune", father_name="Suresh Kumar")
    # WARNING: password hash is dummy; register endpoint will create a real one if needed.
    db.add(u); db.commit(); db.refresh(u)
    print("Seeded user", u.email)
    return u

def seed_samples(user):
    samples = Path("samples/documents")
    for f in samples.glob("*"):
        dest = UPLOAD_DIR / f.name
        shutil.copyfile(f, dest)
        rec = DocumentRecord(user_id=user.id, label="OTHER", file_path=str(dest), mime_type="image/png")
        db.add(rec)
    db.commit()
    print("Seeded documents")
    # seed synonyms
    syn = db.query(Synonym).filter(Synonym.canonical_key=="PARENT_NAME").first()
    if not syn:
        s = Synonym(canonical_key="PARENT_NAME", variants_json=json.dumps(["Father's Name","Guardian Name","Parent","Parent Name"]))
        db.add(s); db.commit()
    print("Seed done")

if __name__ == '__main__':
    u = seed_user()
    seed_samples(u)