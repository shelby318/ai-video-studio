
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AI Video Studio")


@mcp.tool()
def buat_ide_video(
    tema: str,
    platform: str = "YouTube",
    durasi: int = 60
) -> str:
    """Membuat konsep dan ide video."""
    return f"""
AI VIDEO STUDIO - IDE VIDEO
Tema: {tema}
Platform: {platform}
Durasi: {durasi} detik

Buat judul menarik, hook pembuka,
alur cerita, adegan, dan penutup.
"""


@mcp.tool()
def buat_storyboard(
    judul: str,
    cerita: str,
    durasi: int = 60,
    jumlah_klip: int = 6
) -> str:
    """Membuat storyboard video."""
    return f"""
Judul: {judul}
Cerita: {cerita}
Durasi: {durasi} detik
Jumlah klip: {jumlah_klip}

Buat storyboard setiap klip dengan:
visual, aksi karakter, gerakan kamera,
lokasi, pencahayaan, dan transisi.
Jaga konsistensi karakter dan lingkungan.
"""


@mcp.tool()
def prompt_gambar(
    deskripsi: str,
    jenis: str = "Storyboard"
) -> str:
    """Membuat prompt gambar."""
    return f"""
Jenis: {jenis}
Deskripsi: {deskripsi}

Buat prompt gambar detail dengan
karakter, lokasi, komposisi, sudut kamera,
pencahayaan, gaya visual, dan rasio gambar.
"""


@mcp.tool()
def prompt_video(
    deskripsi: str,
    durasi: int = 10
) -> str:
    """Membuat prompt video Google Flow."""
    return f"""
Durasi: {durasi} detik
Adegan: {deskripsi}

Buat prompt video sinematik dengan
gerakan karakter alami, aksi berurutan,
gerakan kamera, lingkungan, pencahayaan,
dan konsistensi visual.
"""


@mcp.tool()
def informasi_aplikasi() -> str:
    """Menampilkan informasi aplikasi."""
    return """
AI VIDEO STUDIO
Versi: 0.1
Fitur:
1. Ide video
2. Storyboard
3. Prompt gambar
4. Prompt Google Flow
"""


if __name__ == "__main__":
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = int(os.environ.get("PORT", "10000"))

    mcp.run(transport="streamable-http")