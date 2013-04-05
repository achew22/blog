aza = function(){};
aza.main = function() {
    return 0; // Exit code
}

/**
 * @copyright Sky Sanders
 * @link http://stackoverflow.com/questions/3177836/how-to-format-time-since-xxx-e-g-4-minutes-ago-similar-to-stack-exchange-site
 *
 * Convert a date to "X units ago"
 */
aza.timeSince = function(since) {
    var date = new Date(since);

    var seconds = Math.floor((new Date() - date) / 1000);

    var interval = Math.floor(seconds / 31536000);

    interval = Math.floor(seconds / 86400);
    if (interval > 3) {
        var months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        var dow = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

        var ord = "th";
        switch (date.getDate()) {
            case 1:
                ord = "st";
                break;
            case 2:
                ord = "nd";
                break;
            case 3:
                ord = "rd";
                break;
        }

        return dow[date.getDay()] + ", " + months[date.getMonth()] + " " + date.getDate() + ord + " " + (1900 + date.getYear());
    } else if (interval > 1) {
        return interval + " days ago";
    }
    interval = Math.floor(seconds / 3600);
    if (interval > 1) {
        return interval + " hours ago";
    }
    interval = Math.floor(seconds / 60);
    if (interval > 1) {
        return interval + " minutes ago";
    }
    return Math.floor(seconds) + " seconds ago";
}