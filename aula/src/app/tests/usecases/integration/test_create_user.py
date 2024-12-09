from infra.user.in_memory_user_repository import InMemoryUserRepository
from unittest.mock import MagicMock
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface
from application.user.create_user_use_case import (
    CreateUserRequest,
    CreateUserResponse,
    CreateUserUseCase,
)
import pytest


class TestCreateUser:
    def test_create_user_with_valid_data(self):
        repository = InMemoryUserRepository()
        use_case = CreateUserUseCase(repository=repository)
        request = CreateUserRequest(name="João")
        response = use_case.execute(request)

        assert len(repository.users) == 1
        assert isinstance(response.id, UUID)

        persited_user = repository.users[0]

        assert persited_user.id == response.id
        assert persited_user.name == "João"
        

   
