from django.db import models

# Create your models here.
class Elevator(models.Model):
    current_floor = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default='stopped')  # Possible values: 'up', 'down', 'stopped'
    is_operational = models.BooleanField(default=True)

    def move_up(self):
        if self.is_operational:
            self.current_floor += 1
            self.status = 'up'
            self.save()
    
    def move_down(self):
        if self.is_operational and self.current_floor > 0:
            self.current_floor -= 1
            self.status = 'down'
            self.save()

    def stop(self):
        self.status = 'stopped'
        self.save()

    def __str__(self):
        return f"Elevator {self.id} on floor {self.current_floor}"
    
class Request(models.Model):
    requested_floor = models.IntegerField()
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for Elevator {self.elevator.id} to floor {self.requested_floor}"

