// this code is a work in progress, it main feature is to add google calendar maintenance event:
// this files located ar google apps script

function addevent(status, location, type, power) {
    //setting:
    var SS = SpreadsheetApp.getActive();
    var sheet = SS.getSheetByName("DB");
    var cal = CalendarApp.getCalendarById(
        "remove-my-calander-id-for-github@group.calendar.google.com"
    );

    var options = {
        description: " סוג הנורה: " + type + " בהספק של: " + power,
        location: location,
    };
    if (status == "cheak report") {
        cal.createAllDayEvent("תיקון תאורה:", new Date(), options);
    }
}
