package meetup

import "time"

type WeekSchedule int

const (
	Last   WeekSchedule = 0
	First  WeekSchedule = 1
	Second WeekSchedule = 8
	Teenth WeekSchedule = 13
	Third  WeekSchedule = 15
	Fourth WeekSchedule = 22
)

func Day(wSched WeekSchedule, wDay time.Weekday, month time.Month, year int) int {
	var date time.Time
	if wSched != Last {
		date = time.Date(year, month, int(wSched), 0, 0, 0, 0, time.UTC)
	} else {
		if month == 12 {
			year++
			month = 1
		} else {
			month++
		}
		date = time.Date(year, month, 1, 0, 0, 0, 0, time.UTC).AddDate(0, 0, -7)
	}
	curWeekday := date.Weekday()
	shift := (7 + int(wDay) - int(curWeekday)) % 7
	date = date.AddDate(0, 0, shift)
	return date.Day()

}
