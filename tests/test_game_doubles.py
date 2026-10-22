import pygame


from src.bullet import Bullet
from src.desconto import Pedido
from src.game_event_handler import GameEventHandler
from tests.doubles import StubSemDesconto


class StubSettings:
    bullet_color = (0, 0, 0)
    bullet_width = 4
    bullet_height = 8
    bullet_speed = 2


class StubShip:
    def __init__(self):
        self.rect = pygame.Rect(40, 80, 20, 20)


def test_pedido_total_with_stub():
    """Verifica o pedido com o stub definido no material da aula."""
    pedido = Pedido(StubSemDesconto())

    assert pedido.total(100) == 100


def test_pedido_total_with_mock(mocker):
    """Verifica o pedido e as interações esperadas com o desconto."""
    desconto = mocker.Mock()
    desconto.calcular.return_value = 10
    pedido = Pedido(desconto)

    resultado = pedido.total(100)

    assert resultado == 90
    desconto.calcular.assert_called()
    desconto.calcular.assert_called_once_with(100)
    assert desconto.calcular.call_count == 1


def test_bullet_moves_using_stub_dependencies():
    """Verifica o movimento do projétil com dependências simples (stub)."""
    screen = pygame.Surface((100, 100))
    ship = StubShip()
    bullet = Bullet(screen, StubSettings(), ship)
    initial_y = bullet.rect.y

    bullet.update()

    assert bullet.rect.y == initial_y - 2


def test_space_key_uses_bullet_manager_mock(mocker):
    """Verifica se a tecla de disparo chama o gerenciador uma vez (mock)."""
    ship = mocker.Mock()
    bullet_manager = mocker.Mock()
    handler = GameEventHandler(ship, bullet_manager)
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)

    handler._handle_keydown(event)

    bullet_manager.fire_bullet.assert_called_once_with()
