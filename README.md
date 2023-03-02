## URLs and API endpoints

# Token auth endpoints
/api-token-auth/    (DRF token - supply username and password in body of POST)
/auth/              (Prefix for Djoser endpoints)

# Menu API endpoints
("?page=" can be added to end of URL to specify page. Shows 2 items per page.)
/api/restaurant/menu
/api/restaurant/menu/<int:pk>

# Booking API endpoints
(Authentication with token required)
/api/restaurant/booking/tables
