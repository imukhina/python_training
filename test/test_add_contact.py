# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first="First", middle="Middle", last="Last", nick="nick", title="title", company="comp", address="London 212 Baker st", home="home", mob="79031022180", work="352524524", fax="32545245", homephone="3224545", email="fgdfhgdf@fd.jh", homepage="www.ya.ru", birthyear="1984", note="Note"))
    app.session.logout()

