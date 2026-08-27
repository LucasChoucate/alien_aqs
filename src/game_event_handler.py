import pygame

class GameEventHandler:
    """Responsável apenas por ler e tratar os eventos do teclado/janela."""

    def __init__(self, ship, bullet_manager) -> None:
        self.ship = ship
        self.bullet_manager = bullet_manager

    def check_events(self) -> None:
        """Responde a eventos de teclado e fechamento da janela."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)

            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event) -> None:
        """Responde a eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self.bullet_manager.fire_bullet()

    def _handle_keyup(self, event) -> None:
        """Responde a eventos de soltura de teclas."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

