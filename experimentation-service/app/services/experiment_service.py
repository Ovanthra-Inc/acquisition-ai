from sqlalchemy.orm import Session
from app.models.experiment import Experiment, ExperimentVariant
from uuid import UUID

class ExperimentService:
    def create_experiment(self, db: Session, user_id: UUID, campaign_id: UUID, experiment_type: str):
        experiment = Experiment(
            user_id=user_id,
            campaign_id=campaign_id,
            experiment_type=experiment_type,
            status="running"
        )
        db.add(experiment)
        db.commit()
        db.refresh(experiment)
        return experiment

    def add_variant(self, db: Session, experiment_id: UUID, variant_name: str, configuration: dict):
        variant = ExperimentVariant(
            experiment_id=experiment_id,
            variant_name=variant_name,
            configuration=configuration
        )
        db.add(variant)
        db.commit()
        db.refresh(variant)
        return variant

    def get_experiment(self, db: Session, experiment_id: UUID):
        return db.query(Experiment).filter(Experiment.id == experiment_id).first()

    def get_variants(self, db: Session, experiment_id: UUID):
        return db.query(ExperimentVariant).filter(ExperimentVariant.experiment_id == experiment_id).all()

    def conclude_experiment(self, db: Session, experiment_id: UUID):
        exp = self.get_experiment(db, experiment_id)
        if exp:
            exp.status = "concluded"
            db.commit()
        return exp
