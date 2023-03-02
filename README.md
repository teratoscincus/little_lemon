# URLs and API endpoints

## Token auth endpoints
### DRF token URL
#### supply username and password in body of POST request
/api-token-auth/
### Prefix for Djoser endpoints
/auth/

## Menu API endpoints
### URL
/api/restaurant/menu

/api/restaurant/menu/<int:pk>

### Pagination
"?page=" can be added to end of URL to specify page. Shows 2 items per page.
#### Example
/api/restaurant/menu?page=1

## Booking API endpoints
#### Authentication with token required
### URL
/api/restaurant/booking/tables
