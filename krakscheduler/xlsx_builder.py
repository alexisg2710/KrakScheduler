from asyncio import current_task
from decimal import ROUND_DOWN
import xlsxwriter
from datetime import datetime
from datetime import timedelta

def build_schedule(event):
    wb = xlsxwriter.Workbook('schedule.xlsx')
    global_sheet = wb.add_worksheet('Global')
    individual_sheet = wb.add_worksheet('Individual')

    #build_global_sheet_skeleton(global_sheet, time_slots, stands)
    #build_individual_sheet_skeleton(individual_sheet, time_slots, workers)

    build_stands_names(global_sheet, event.get_stands_list())
    build_hours_slots(global_sheet, event)

    return (wb, global_sheet, individual_sheet)

def build_global_sheet_skeleton(sheet, time_slots, stands):
    row = 1
    col = 1

    for time_slot in time_slots:
        sheet.write(row, 0, time_slot)
        row += 1

    for stand, _ in stands:
        sheet.write(0, col, stand)
        col += 1

def build_individual_sheet_skeleton(sheet, time_slots, workers):
    row = 1
    col = 1

    for time_slot in time_slots:
        sheet.write(0, col, time_slot)
        col += 1

    for worker in workers:
        sheet.write(row, 0, worker)
        row += 1

def fill_global_sheet(sheet, duration, schedule):
    row = 1
    col = 1

    for stand in schedule:
        workers = '\n'.join(schedule[stand])
        for slot in range(0, duration):
            sheet.write(row, col, workers)
            col += 1
        col = 1
        row += 1

def build_stands_names(sheet, stands_list):
    row = 0
    col = 1

    for stand in stands_list:
        sheet.write(row, col, stand.get_name())
        col += 1

def build_hours_slots(sheet, event):
    row = 1
    col = 0
    time_format = '%H:%M'

    start_current_shift = event.get_start_hour()

    duration = event.get_event_hours_duration()
    print(duration)
    print(type(duration))
    for i in range (duration):
        end_current_shift = start_current_shift + timedelta(hours = 1)
        sheet.write(row, col, start_current_shift.strftime(time_format) + " - " + end_current_shift.strftime(time_format))
        row += 1
        start_current_shift = end_current_shift

#def add_workers(sheet, stand, shift, worker):
