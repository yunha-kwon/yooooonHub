def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        min_dist_sq = float('inf')
        reflections = [
            (ballX, -ballY),
            (ballX, 2 * n - ballY),
            (-ballX, ballY),
            (2 * m - ballX, ballY)
        ]
        for rx, ry in reflections:
            dx = rx - startX
            dy = ry - startY
            dist_sq = dx * dx + dy * dy

            # 같은 세로선 상에서 위아래로 직선 충돌
            if startX == ballX and startY != ballY:
                if (startY < ballY and ry > ballY) or (startY > ballY and ry < ballY):
                    continue

            # 같은 가로선 상에서 좌우로 직선 충돌
            if startY == ballY and startX != ballX:
                if (startX < ballX and rx > ballX) or (startX > ballX and rx < ballX):
                    continue

            if startX == ballX and startY == ballY:
                continue  # 출발 위치와 동일 → 무효

            min_dist_sq = min(min_dist_sq, dist_sq)

        answer.append(min_dist_sq)

    return answer
