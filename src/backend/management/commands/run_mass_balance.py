from django.core.management.base import BaseCommand
from backend.data import models
from backend.domain import mass_balance

class Command(BaseCommand):
    help = 'Run mass balance calculation for a given design'

    # def add_arguments(self, parser):
    #     parser.add_argument('design_id', type=int, help='ID of the design')

    def handle(self, *args, **kwargs):
        # design_id = kwargs['design_id']
        try:
            # design = models.Design.objects.get(id=1)
            # mass_balance.calculate_process_outputs(design)
            mass_balance.calculate_process_outputs
        except models.Design.DoesNotExist:
            self.stderr.write(f'Design with id {1} does not exist')