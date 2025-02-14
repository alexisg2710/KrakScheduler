import random

class Scheduler:
    schedule = {}

    def __init__(self, event):
        # Event object
        self.event = event
        # Stand object list
        self.stands_list = event.get_stands_list()
        # Worker object list
        self.staffs_list = event.get_staffs_list()
        # list that will hold x histogram of taken staff for every hour
        # for an event of 7 hour it will hold 7 histogram for example
        self.taken_staffs = self.init_taken_staffs()

    def init_taken_staffs(self):
        taken_staffs = []
        for i in range(self.event.get_event_hours_duration()):
            taken_staffs.append([0]* len(self.staffs_list))
        return taken_staffs

    def get_workers_for_stand(self, stand, duration):
        name, quantity = stand
        quantity = quantity if quantity <= len(self.workers) else len(self.workers)

        current_workers = random.sample(self.workers, quantity)
        self.schedule[name] = current_workers

    def fill_schedule(self):
        for stand in self.stands:
            self.get_workers_for_stand(stand, len(self.time_slots))

    def get_schedule(self):
        return self.schedule

    # return the number of places left for the specific stand at a specific shift
    def get_current_shift_remaining_places(self, shift_index, stand):
        return stand.get_free_places(shift_index)

    # return the number of places taken for the specific stand at a specific shift
    def get_current_shift_taken_places(self, shift_index, stand):
        return stand.get_taken_places(shift_index)

    # return the list of current workers at a specific stand and at a specific shift
    def get_current_shift_worker_list(self, shift_index, stand):
        return stand.get_worker_list(shift_index)

    #def create_stands_columns(self, nb_stands, stands_lists)
