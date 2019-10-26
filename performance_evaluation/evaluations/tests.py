from datetime import datetime

from django.test import TestCase
from model_bakery import baker

from .models import Evaluation, EvaluationSkill


class TestEvalutaionModel(TestCase):
    def setUp(self):
        self.evaluation = baker.make(Evaluation)

    def test_average(self):
        baker.make(EvaluationSkill, evaluation=self.evaluation, grade=2)
        baker.make(EvaluationSkill, evaluation=self.evaluation, grade=4)

        self.assertEqual(self.evaluation.average(), 3)

    def test_default_year_is_current_year(self):
        now = datetime.now()
        self.assertEqual(now.year, self.evaluation.year)
