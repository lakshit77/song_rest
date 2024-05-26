from song_app.consts import STATUS_CODE, MESSAGE, SUCCESS_CODE, FAILURE_CODE

success = {STATUS_CODE: SUCCESS_CODE, MESSAGE: "Success"}
generic_error_1 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Invalid request details"}
generic_error_2 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Please try again after sometime"}
generic_error_3 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Invalid response"}

rating_validation = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Star rating must be between 0 and 5."}
