# Math Quiz App

## Deskripsi

Sebuah aplikasi GUI berbasis Python yang berisi soal hitung-hitungan matematika, mulai dari matematika dasar, aljabar, deret, kalkulus, dsb. Soal dibuat secara otomatis melalui generators yang ada.   

## Instalasi

Clone repository github

```bash
git clone https://github.com/FulDX/TA_PROGDAS_MUHAMMAD-ZAKI-ANWAR-FIRDAUS_21120125130074_MathQuizApp-Aplikasi-Latihan-Soal-Matematika.git
```

Lalu install requirements

```bash
pip install -r requirements.txt
```


Untuk menjalankan:
```bash
python run.py
```

## Tutorial Penulisan Jawaban

Aplikasi ini menggunakan notasi matematika yang dapat diinterpretasikan oleh SymPy. Berikut adalah panduan penulisan jawaban untuk berbagai jenis soal:

### 1. Notasi Dasar

| Operasi | Notasi |
|---------|--------|
| Penjumlahan | `a + b` |
| Pengurangan | `a - b` |
| Perkalian | `a * b` atau `ab` (perkalian implisit) |
| Pembagian | `a / b` |
| Pangkat | `a ** b` atau `a^b` |
| Akar kuadrat | `sqrt(a)` |

**Contoh:**
- Perkalian: `2 * 3` atau `2x` atau `(x+1)(x-1)`
- Pangkat: `x ** 2` atau `x^2`
- Akar: `sqrt(25)` atau `sqrt(x+1)`

### 2. Konstanta & Simbol

| Elemen | Penulisan |
|--------|-----------|
| $\pi$ | `pi` |
| $e$ (Euler) | `e` |
| Tak terhingga | `oo` atau `inf` atau `infinity` atau `∞` |
| Variabel | `x`, `y`, `z`, dll |

**Contoh:**
- $\pi$ dalam perhitungan: `pi` atau `pi/2` untuk $\frac{\pi}{2}$
- Tak terhingga: `oo` atau `-oo`

### 3. Fungsi Trigonometri

| Fungsi | Notasi |
|--------|--------|
| Sinus | `sin(x)` |
| Kosinus | `cos(x)` |
| Tangen | `tan(x)` |
| Sekan | `sec(x)` |
| Kosekan | `csc(x)` |
| Kotangen | `cot(x)` |
| Invers Sinus | `asin(x)` atau `arcsin(x)` |
| Invers Kosinus | `acos(x)` atau `arccos(x)` |
| Invers Tangen | `atan(x)` atau `arctan(x)` |

**Contoh:**
- $\sin(\pi/2)$ → `sin(pi/2)`
- $\arccos(0.5)$ → `arccos(0.5)` atau `acos(0.5)`
- $\tan(x)$ → `tan(x)`

### 4. Fungsi Logaritma & Eksponensial

| Fungsi | Notasi |
|--------|--------|
| Logaritma natural | `log(x)` atau `ln(x)` |
| Logaritma basis 10 | `log(x, 10)` |
| Eksponensial | `exp(x)` atau `e**x` |

**Contoh:**
- $\ln(x)$ → `log(x)` atau `ln(x)`
- $e^x$ → `exp(x)` atau `e**x`
- $\log_{10}(100)$ → `log(100, 10)`

### 5. Persamaan Linier

Untuk persamaan yang meminta jawaban dalam bentuk $x = ...$, Anda dapat menuliskan:

**Format:**
- `x = nilai` atau
- `nilai` (hanya nilai saja)

**Contoh:**
- Jika soal: $3x + 5 = 20$
- Jawaban: `5` atau `x = 5`

### 6. Persamaan Kuadratik (Dua Solusi)

Untuk persamaan kuadratik yang memiliki 2 solusi, **harus memberikan kedua jawaban** yang dipisahkan oleh koma atau titik koma:

**Format:**
```
jawaban1, jawaban2
```
atau
```
jawaban1; jawaban2
```

**Contoh:**
- Jika soal: $x^2 - 5x + 6 = 0$
- Jawaban benar: `2, 3` atau `3, 2` (urutan tidak penting)
- Jawaban salah: `2` (hanya satu solusi) 

### 7. Integral Tak Tentu

Untuk integral tak tentu $\int f(x) \, dx$, jawaban **tidak perlu menyertakan konstanta integrasi** $C$. Sistem akan membandingkan turunan dari jawaban Anda dengan turunan jawaban yang benar.

**Format:**
```
fungsi_hasil_integrasi
```

**Contoh:**
- Jika soal: $\int 2x \, dx$
- Jawaban: `x**2` atau `x^2` (tidak perlu + C)

### 8. Integral Tentu

Untuk integral tentu $\int_a^b f(x) \, dx$, jawaban harus berupa **nilai numerik** saja.

**Format:**
```
nilai_numerik
```

**Contoh:**
- Jika soal: $\int_0^1 2x \, dx$
- Jawaban: `1` atau `1.0`

### 9. Limit

Untuk soal limit, jawaban bisa berupa nilai atau tak terhingga:

**Format:**
```
nilai
```
atau
```
oo, -oo, inf
```

**Contoh:**
- $\lim_{x \to 2} (x + 3) = 5$ → `5`
- $\lim_{x \to \infty} x^2 = \infty$ → `oo` atau `infinity`

### 10. Ekspresi Kompleks

Anda dapat menggabungkan berbagai notasi untuk membuat ekspresi kompleks:

**Contoh:**
- $\frac{x^2 + 1}{x - 1}$ → `(x**2 + 1)/(x - 1)`
- $\sqrt{\sin(x)}$ → `sqrt(sin(x))`
- $e^{-x^2}$ → `exp(-x**2)` atau `e**(-x^2)`
- $\frac{\pi}{4} + \frac{x}{2}$ → `pi/4 + x/2`

### 11. Tips & Trik

✅ **Boleh dilakukan:**
- Menggunakan tanda kurung: `(x + 1) * (x - 1)`
- Spasi tidak masalah: `x ** 2` atau `x**2`
- Perkalian implisit: `2x` atau `2 * x` (keduanya ok)
- Format alternatif: `ln(x)` atau `log(x)` untuk natural log
- Camelcase fungsi: `Sin(x)` atau `sin(x)` (keduanya ok)

❌ **Jangan dilakukan:**
- Menulis pangkat dengan simbol `²`: `x²` ❌ → gunakan `x**2` ✅
- Garis pecahan HTML: `<sup>` atau `<sub>` ❌
- Simbol khusus LaTeX inline: `\sqrt{x}` atau `\frac{a}{b}` ❌
- Lupa tanda kurung: `2x + 1 / 2` (bisa ambigu) → gunakan `(2*x + 1) / 2` ✅

### 12. Format Jawaban Ganda

Jika ada beberapa jawaban yang benar (alternatif), tulislah dengan koma:

**Contoh:**
- Jawaban untuk $|x| = 5$: `5, -5` atau `-5, 5`
- Jawaban untuk $\sin(x) = 1$ (dalam $[0, 2\pi]$): `pi/2`

---

**Catatan:** Jika jawaban ditolak meski menurut Anda benar, coba format alternatif atau periksa apakah Anda memahami soal dengan benar.