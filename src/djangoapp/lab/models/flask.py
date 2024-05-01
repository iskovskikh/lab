from django.db import models

from djangoapp.common.models import BaseEntityModel
from djangoapp.lab.models.lifecase import LifeCaseModel
from laboratory.lifecase.domain.entities.flask import Flask
from laboratory.lifecase.domain.value_objects import FlaskId


class FlaskModel(BaseEntityModel[Flask]):
    id = models.UUIDField(primary_key=True)
    lifecase = models.ForeignKey(LifeCaseModel, on_delete=models.CASCADE, related_name='flasks')
    pieces_count = models.IntegerField()
    pieces_count_to_work = models.IntegerField()

    # defect: FlaskDefectVO | None = None

    def to_domain(self) -> Flask:
        flask = Flask(
            id=FlaskId(str(self.id)),
            pieces_count=self.pieces_count,
            pieces_count_to_work=self.pieces_count_to_work
        )
        return flask

    @staticmethod
    def from_domain(entity: Flask, lifecase: LifeCaseModel) -> 'FlaskModel':  # type: ignore[override]
        item, _ = FlaskModel.objects.get_or_create(
            id=entity.id,
            defaults=dict(
                lifecase=lifecase,
                pieces_count=entity.pieces_count,
                pieces_count_to_work=entity.pieces_count_to_work,
            )
        )

        return item
