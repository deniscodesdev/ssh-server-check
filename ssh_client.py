import asyncssh


async def connect(host: str, username: str, password: str):
    return await asyncssh.connect(
        host=host,
        username=username,
        password=password,
        known_hosts=None,
    )


async def run_command(conn, command: str):
    result = await conn.run(command, check=False)
    return result.stdout.strip()