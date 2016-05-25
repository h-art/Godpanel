TEST_FIXTURES = ('test_data',)
TEST_USERNAME = 'test'
TEST_PASSWORD = 'testpassword'
EMPLOYEES_RESPONSE_FIELDS = {'id', 'area', 'role', 'title'}
ALLOCATIONS_RESPONSE_FIELDS = {'id', 'resourceId', 'start', 'end',
                               'saturation', 'title', 'client', 'project_id',
                               'allocation_type', 'note'}
HTTP_OK = 200
HTTP_FORBIDEN = 403
HTTP_REDIRECT = 302
