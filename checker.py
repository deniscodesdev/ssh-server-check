from rich.console import Console
from rich.table import Table

from ssh_client import connect, run_command

console = Console()


async def check_server(host: str, username: str, password: str):
    console.print("[cyan]Connecting...[/cyan]")

    try:
        async with await connect(host, username, password) as conn:

            table = Table(title="SSH Server Information")

            table.add_column("Parameter", style="cyan")
            table.add_column("Value", style="green")

            os_name = await run_command(conn, "cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2")
            uptime = await run_command(conn, "uptime -p")
            cpu = await run_command(conn, "nproc")
            ram = await run_command(conn, "free -h | awk '/Mem:/ {print $2}'")
            disk = await run_command(conn, "df -h / | awk 'NR==2 {print $2}'")
            kernel = await run_command(conn, "uname -r")
            hostname = await run_command(conn, "hostname")

            table.add_row("Hostname", hostname)
            table.add_row("OS", os_name.replace('"', ""))
            table.add_row("Kernel", kernel)
            table.add_row("CPU Cores", cpu)
            table.add_row("RAM", ram)
            table.add_row("Disk", disk)
            table.add_row("Uptime", uptime)

            console.print(table)

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")