import pygame
import os
import random

pygame.init() # 초기화 (반드시 필요)

# 경로 설정
current_path = os.getcwd()

# 화면 크기 설정
screen_width = 720
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('똥피하기')

# BGM
pygame.mixer.music.load(os.path.join(current_path, 'bgm.mp3'))
pygame.mixer.music.play(-1, 1)

# FPS
clock = pygame.time.Clock()

# 배경이미지 설정
background = pygame.image.load(os.path.join(current_path, 'quiz_background.jpg'))

# 캐릭터 스프라이트 불러오기
character = pygame.image.load(os.path.join(current_path, 'quiz_character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# 이동좌표
to_x_LEFT = 0
to_x_RIGHT = 0

# 이동속도
character_speed = 0.6

# 적 캐릭터 불러오기
enemy = pygame.image.load(os.path.join(current_path, 'quiz_enemy.png'))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0, screen_width - enemy_width)
enemy_y_pos = 0

# 적 이동좌표(속도)
enemy_to_y = 1

# 복수의 적 생성
enemies = []

# 랜덤한 시간에 적 출현 (최초 시작부터 3초안에는 적어도 적 1가 나오도록)
appearance_time = []
appearance_time.append(random.randrange(0, 3))

# 피한 갯수 카운트
game_font = pygame.font.SysFont('malgungothic', 24)
count = 0

# 데드이미지
dead = pygame.image.load(os.path.join(current_path, 'quiz_dead.png'))

##########################################################################################################

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # fps설정

    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # 이벤트 루프 실행
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            pygame.mixer.music.stop()
            running = False # 이벤트 루프 종료

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_RIGHT += character_speed
        
        if event.type == pygame.KEYUP:
            to_x_LEFT = 0
            to_x_RIGHT = 0

    character_x_pos += to_x_LEFT * dt + to_x_RIGHT * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 적을 등장시간에 맞춰 출현
    elapsed_time = int(pygame.time.get_ticks()/1000)
    if elapsed_time == appearance_time[-1]:
        appearance_time.append(random.randrange(elapsed_time, elapsed_time + 2)) # 적어도 2초 안에는 적이 출현하도록
        del(appearance_time[0]) # 메모리 부하 방지
        enemies.append([random.randrange(0, screen_width - enemy_width), 0])

    # 적 위치 조정
    enemies = [[e[0], e[1] + enemy_to_y * dt] for e in enemies]

    # 카운트 작동
    for e in enemies:
        if e[1] >= screen_height:
            count += 1

    # 지나간 적 없애기
    enemies = [[e[0], e[1]] for e in enemies if e[1] < screen_height]

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    screen.blit(background, (0, 0)) # 배경 이미지 그리기, 위치설정
    # screen.fill((0, 0, 255)) # 배경색 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기, 위치설정
    for e in enemies:
        screen.blit(enemy, (e[0], e[1]))

    # 충돌체크
    for e in enemies:
        enemy_x_pos = e[0]
        enemy_y_pos = e[1]
        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        if character_rect.colliderect(enemy_rect):
            # 데드모션
            screen.blit(dead, (character_x_pos, character_y_pos))
            # 게임결과
            game_result = game_font.render("아이쿠! %d개 피하셨네요!" % count, True, (0, 0, 0))
            msg_rect = game_result.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(game_result, msg_rect)
            # 효과음, BGM 멈춤, 게임 정지
            pygame.mixer.music.stop()
            dead_SE = pygame.mixer.Sound(os.path.join(current_path, 'dead_effect.mp3'))
            dead_SE.play()
            running = False

    # 피한 갯수 표시
    counter = game_font.render('피한 갯수 : %d' % count, True, (0, 0, 0))
    screen.blit(counter, (10, 10))

    pygame.display.update() # 게임 화면 업데이트

# 게임 종료 후 잠시 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()