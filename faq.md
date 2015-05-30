Frequently Asked Questions
==========================

## Why are streams with barely any viewers showing up?

I couldn't tell you why. Twitch will sometimes give bad responses to API calls, 
it's entirely out of my hands as to what Twitch will give back.

## Why don't certain streams show up at all?

I had this problem for a while, after tinkering around, it turns out the issue 
is Twitch's API with the 'limit' field. Anything less than 20 usually fails to 
retrieve most streams properly, so I set the DEFAULT_LIMIT to 20 to make up for 
this issue.

