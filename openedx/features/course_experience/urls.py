"""
Defines URLs for the course experience.
"""

from django.conf.urls import url

from views.course_home import CourseHomeFragmentView, CourseHomeView
from views.course_outline import CourseOutlineFragmentView
from views.course_reviews import CourseReviewsView
from views.course_updates import CourseUpdatesFragmentView, CourseUpdatesView
from views.course_sock import CourseSockFragmentView
from views.digital_locker_fragment import DigitalLockerFragmentView 
from views.digital_locker import DigitalLockerView
from views.latest_update import LatestUpdateFragmentView
from views.welcome_message import WelcomeMessageFragmentView, dismiss_welcome_message

urlpatterns = [
    url(
        r'^$',
        CourseHomeView.as_view(),
        name='openedx.course_experience.course_home',
    ),
    url(
        r'^updates$',
        CourseUpdatesView.as_view(),
        name='openedx.course_experience.course_updates',
    ),
    url(
        r'^reviews$',
        CourseReviewsView.as_view(),
        name='openedx.course_experience.course_reviews',
    ),
    url(
        r'^digital_locker',
        DigitalLockerView.as_view(),
        name='openedx.course_experience.digital_locker',
    ),
    url(
        r'^home_fragment$',
        CourseHomeFragmentView.as_view(),
        name='openedx.course_experience.course_home_fragment_view',
    ),
    url(
        r'^outline_fragment$',
        CourseOutlineFragmentView.as_view(),
        name='openedx.course_experience.course_outline_fragment_view',
    ),
    url(
        r'^updates_fragment$',
        CourseUpdatesFragmentView.as_view(),
        name='openedx.course_experience.course_updates_fragment_view',
    ),
    url(
        r'^digital_locker_fragment',
        DigitalLockerFragmentView.as_view(),
        name='openedx.course_experience.digital_locker_fragment',
    ),
    url(
        r'^welcome_message_fragment$',
        WelcomeMessageFragmentView.as_view(),
        name='openedx.course_experience.welcome_message_fragment_view',
    ),
    url(
        r'^latest_update_fragment$',
        LatestUpdateFragmentView.as_view(),
        name='openedx.course_experience.latest_update_fragment_view',
    ),
    url(
        r'course_sock_fragment$',
        CourseSockFragmentView.as_view(),
        name='openedx.course_experience.course_sock_fragment_view',
    ),
    url(
        r'^dismiss_welcome_message$',
        dismiss_welcome_message,
        name='openedx.course_experience.dismiss_welcome_message',
    ),
]
