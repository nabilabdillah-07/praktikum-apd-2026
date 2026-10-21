"""
Flowchart program Profit Item Blade Ball (PT-5)
Output: flowchart_blade_ball.pdf
Jalankan:  pip install reportlab && python flowchart_blade_ball.py
"""
import math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white, black, HexColor

W, H = 842, 1191                       # A3 portrait
def Y(v): return H - v                 # v = jarak dari atas

C_RED  = HexColor('#B22222')
C_GREY = HexColor('#555555')
FS = 7.2

# ---------------- node ----------------
class Node:
    def __init__(self, kind, cx, cy, w, h, lines, fs=FS):
        self.kind, self.cx, self.cy = kind, cx, cy
        self.w, self.h, self.lines, self.fs = w, h, lines, fs
    def top(self):    return (self.cx, self.cy - self.h/2)
    def bottom(self): return (self.cx, self.cy + self.h/2)
    def left(self):   return (self.cx - self.w/2, self.cy)
    def right(self):  return (self.cx + self.w/2, self.cy)

def N(kind, cx, cy, w, h, lines, fs=FS):
    return Node(kind, cx, cy, w, h, lines, fs)

def _text(c, n):
    c.setFillColor(black); c.setFont('Helvetica', n.fs)
    lh = n.fs + 2.5
    y0 = Y(n.cy) + (len(n.lines)-1)*lh/2 - n.fs*0.35
    for i, ln in enumerate(n.lines):
        c.drawCentredString(n.cx, y0 - i*lh, ln)

def draw_node(c, n):
    c.setStrokeColor(C_RED); c.setFillColor(white); c.setLineWidth(1)
    x, y, w, h = n.cx, Y(n.cy), n.w, n.h
    if n.kind == 'term':
        c.roundRect(x-w/2, y-h/2, w, h, h/2, fill=1, stroke=1)
    elif n.kind == 'io':
        s = 12
        p = c.beginPath()
        p.moveTo(x-w/2+s, y+h/2); p.lineTo(x+w/2, y+h/2)
        p.lineTo(x+w/2-s, y-h/2); p.lineTo(x-w/2, y-h/2)
        p.close(); c.drawPath(p, fill=1, stroke=1)
    elif n.kind == 'dec':
        p = c.beginPath()
        p.moveTo(x, y+h/2); p.lineTo(x+w/2, y)
        p.lineTo(x, y-h/2); p.lineTo(x-w/2, y)
        p.close(); c.drawPath(p, fill=1, stroke=1)
    else:
        c.rect(x-w/2, y-h/2, w, h, fill=1, stroke=1)
    _text(c, n)

def arrow(c, pts, head=True, color=C_RED):
    c.setStrokeColor(color); c.setFillColor(color); c.setLineWidth(0.9)
    P = [(x, Y(y)) for x, y in pts]
    p = c.beginPath(); p.moveTo(*P[0])
    for q in P[1:]: p.lineTo(*q)
    c.drawPath(p, fill=0, stroke=1)
    if head:
        x1, y1 = P[-2]; x2, y2 = P[-1]
        dx, dy = x2-x1, y2-y1
        L = math.hypot(dx, dy) or 1
        ux, uy = dx/L, dy/L
        sz = 6; px, py = -uy, ux
        a = (x2-ux*sz+px*sz*0.5, y2-uy*sz+py*sz*0.5)
        b = (x2-ux*sz-px*sz*0.5, y2-uy*sz-py*sz*0.5)
        q = c.beginPath(); q.moveTo(x2, y2); q.lineTo(*a); q.lineTo(*b); q.close()
        c.drawPath(q, fill=1, stroke=0)

def label(c, x, y, text, fs=6, color=C_GREY):
    c.setFillColor(color); c.setFont('Helvetica-Bold', fs)
    c.drawString(x, Y(y), text)

# ---------------- header / footer ----------------
def header(c):
    c.setFillColor(C_RED); c.rect(0, Y(42), W, 42, fill=1, stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold', 14)
    c.drawCentredString(W/2, Y(18), 'FLOWCHART — PROFIT ITEM BLADE BALL')
    c.setFont('Helvetica', 9)
    c.drawCentredString(W/2, Y(33),
        'Program Manajemen Data Penjualan & Profit  (Login, Register, CRUD, Role-based)')
    c.setFillColor(C_GREY); c.setFont('Helvetica-Oblique', 7)
    c.drawString(25, Y(58), 'Catatan: panah berlabel "loop" kembali ke titik loop sebelumnya. '
                            'Validasi: nama tidak kosong, harga harus angka (isdigit).')
    c.setStrokeColor(C_RED); c.setLineWidth(1); c.line(25, Y(1155), W-25, Y(1155))
    c.setFillColor(C_GREY); c.setFont('Helvetica', 7)
    c.drawString(25, Y(1167),
        'Muhammad Nabil Abdillah  |  NIM 2609106047  |  PT-5')
    c.drawRightString(W-25, Y(1167), 'Algoritma Pemrograman Dasar')

# ---------------- isi flowchart ----------------
def halaman(c):
    header(c)

    # -------- NODES --------
    # center (cx=400)
    start     = N('term', 400,  85, 100, 28, ['Start'])
    init      = N('proc', 400, 140, 340, 55,
                  ['dataUser: admin, nabil',
                   'dataPenjualan: 2 item',
                   'idBerikutnya = 3'])
    menuUtama = N('io',   400, 220, 340, 55,
                  ['Clear screen',
                   'Menu: 1.Login 2.Register 3.Keluar'])
    inPilih   = N('io',   400, 295, 200, 32, ['Input pilih'])
    dPilih    = N('dec',  400, 365, 240, 80, ['pilih?', '(1/2/3/lain)'])
    end       = N('term', 400, 455, 100, 28, ['End'])
    errPilih  = N('io',   520, 455, 140, 32, ['Pilihan tidak ada'])

    # login (cx=150)
    inLogin   = N('io',   150, 455, 200, 40, ['Input username', '& password'])
    dLogin    = N('dec',  150, 535, 180, 70, ['Login valid?'])
    errLogin  = N('io',    60, 625,  90, 45, ['Username/', 'password salah'])
    roleN     = N('proc', 150, 635, 180, 32, ['role = user.role'])
    menuRole  = N('io',   145, 710, 270, 65,
                  ['Clear screen', 'Menu role:',
                   'admin: 1-5 | user: 2 & 5'])
    inMenu    = N('io',   150, 790, 180, 32, ['Input menu'])
    chkAdmin  = N('dec',  150, 865, 220, 80, ['role=user AND', 'menu in {1,3,4}?'])
    errAdmin  = N('io',   380, 865, 130, 40, ['Menu cuma', 'buat admin'])
    chk1234   = N('dec',  150, 955, 220, 70, ['menu in', '{1,2,3,4}?'])
    proc1234  = N('proc', 450, 955, 280, 115,
                  ['Proses menu:',
                   '1.Tambah: input→validasi→simpan',
                   '2.Lihat: tampilkan list+profit',
                   '3.Ubah: pilih no→input→validasi',
                   '4.Hapus: pilih no→hapus'])
    chk5      = N('dec',  150, 1050, 200, 70, ['menu = 5?'])
    logout    = N('proc', 350, 1050, 130, 32, ['Logout'])
    errMenu   = N('io',   150, 1125, 200, 40, ['Pilihan ga ada'])

    # register (cx=710)
    inReg     = N('io',   710, 455, 140, 40, ['Input username', '& password baru'])
    dReg      = N('dec',  710, 535, 140, 80, ['Kosong/', 'sudah ada?'])
    errReg    = N('io',   530, 535, 120, 40, ['Validasi', 'gagal'])
    saveReg   = N('proc', 710, 620, 160, 40, ['Simpan user', 'baru (role=user)'])

    nodes = [start, init, menuUtama, inPilih, dPilih, end, errPilih,
             inLogin, dLogin, errLogin, roleN, menuRole, inMenu, chkAdmin,
             errAdmin, chk1234, proc1234, chk5, logout, errMenu,
             inReg, dReg, errReg, saveReg]
    for n in nodes:
        draw_node(c, n)

    # -------- ARROWS --------
    # main
    arrow(c, [start.bottom(), init.top()])
    arrow(c, [init.bottom(), menuUtama.top()])
    arrow(c, [menuUtama.bottom(), inPilih.top()])
    arrow(c, [inPilih.bottom(), dPilih.top()])

    # dPilih → 4 cabang
    arrow(c, [(280, 365), (150, 365), (150, 435)])
    label(c, 155, 360, '1. Login')
    arrow(c, [(520, 365), (710, 365), (710, 435)])
    label(c, 525, 360, '2. Register')
    arrow(c, [(400, 405), (400, 441)])
    label(c, 405, 425, '3. Keluar')
    arrow(c, [(470, 390), (520, 390), (520, 439)])
    label(c, 475, 385, 'lain')

    # errPilih loop → menuUtama (kanan)
    arrow(c, [(590, 455), (620, 455), (620, 205), (570, 205)])
    label(c, 600, 340, 'loop', fs=5.5)

    # login
    arrow(c, [inLogin.bottom(), dLogin.top()])
    arrow(c, [(150, 570), (150, 619)]);  label(c, 155, 595, 'Ya')
    arrow(c, [( 60, 535), ( 60, 602)]);  label(c,  20, 575, 'Tidak')

    # errLogin loop → menuUtama (kiri)
    arrow(c, [(15, 625), (5, 625), (5, 205), (230, 205)])

    arrow(c, [roleN.bottom(), menuRole.top()])
    arrow(c, [menuRole.bottom(), inMenu.top()])
    arrow(c, [inMenu.bottom(), chkAdmin.top()])

    # chkAdmin
    arrow(c, [(260, 865), (315, 865)]);  label(c, 265, 858, 'Ya')
    arrow(c, [(380, 845), (380, 725), (280, 725)])     # errAdmin loop
    arrow(c, [(150, 905), (150, 920)]);  label(c, 155, 912, 'Tidak')

    # chk1234
    arrow(c, [(260, 955), (310, 955)]);  label(c, 265, 948, 'Ya')
    arrow(c, [(590, 955), (605, 955), (605, 705), (280, 705)])  # proc loop
    arrow(c, [(150, 990), (150, 1015)]); label(c, 155, 1000, 'Tidak')

    # chk5
    arrow(c, [(250, 1050), (285, 1050)]); label(c, 255, 1043, 'Ya')
    arrow(c, [(150, 1085), (150, 1105)]); label(c, 155, 1095, 'Tidak')

    # errMenu loop → menuRole
    arrow(c, [(250, 1125), (300, 1125), (300, 710), (280, 710)])

    # logout loop → menuUtama
    arrow(c, [(415, 1050), (615, 1050), (615, 235), (570, 235)])

    # register
    arrow(c, [inReg.bottom(), dReg.top()])
    arrow(c, [(710, 575), (710, 600)]);  label(c, 715, 588, 'Ya')
    arrow(c, [(640, 535), (590, 535)]);  label(c, 620, 528, 'Tidak')

    # errReg loop → menuUtama (kanan)
    arrow(c, [(530, 515), (630, 515), (630, 215), (570, 215)])

    # saveReg loop → menuUtama (kanan)
    arrow(c, [(790, 620), (800, 620), (800, 225), (570, 225)])

# ---------------- main ----------------
if __name__ == '__main__':
    out = 'flowchart_blade_ball.pdf'
    cv = canvas.Canvas(out, pagesize=(W, H))
    cv.setTitle('Flowchart Profit Item Blade Ball (PT-5)')
    halaman(cv)
    cv.showPage()
    cv.save()
    print('selesai ->', out)