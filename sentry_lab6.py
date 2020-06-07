import sentry_sdk
from sentry_sdk import configure_scope

sentry_sdk.init("https://7b2d5742527144e5bceddbf509f3671f@o403943.ingest.sentry.io/5267109")

print('Hello World!')

with configure_scope() as scope:
    scope.user = {'email':'egov.66@gmail.com'}
    scope.set_tag("Sentry","Lab_6")
    scope.set_tag("Author","Egovcev Rostislav")

division_by_zero = 1 / 0
