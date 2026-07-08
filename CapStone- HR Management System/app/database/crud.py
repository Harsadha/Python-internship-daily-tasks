from sqlalchemy.orm import Session

from . import models
from .. import schemas

def get_user(db: Session, username: str):
    return (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )

def create_user(db: Session,username: str,hashed_password: str,):
    user = models.User(
        username=username,
        hashed_password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_audit_log(db: Session,log: schemas.AuditLogCreate,):
    audit = models.AuditLog(
        username=log.username,
        action=log.action,
        timestamp=log.timestamp,
    )
    db.add(audit)
    db.commit()
    db.refresh(audit)
    return audit

def get_audit_logs(db: Session):
    return (
        db.query(models.AuditLog)
        .order_by(models.AuditLog.id.desc())
        .all()
    )