import streamlit as st
import math

def hitung_debit_volume_waktu(volume, waktu, satuan_volume="m³", satuan_waktu="s"):
    if satuan_waktu == "menit":
        waktu *= 60
    elif satuan_waktu == "jam":
        waktu *= 3600
    if satuan_volume == "L":
        volume /= 1000
    debit_m3s = volume / waktu
    debit_ls = debit_m3s * 1000
    return {"m³/s": debit_m3s, "L/s": debit_ls}

def hitung_luas_penampang_lingkaran(diameter):
    return math.pi * (diameter / 2) ** 2

def hitung_luas_penampang_persegi(panjang, lebar):
    return panjang * lebar

def hitung_debit_luas_kecepatan(luas_penampang, kecepatan):
    debit_m3s = luas_penampang * kecepatan
    debit_ls = debit_m3s * 1000
    return {"m³/s": debit_m3s, "L/s": debit_ls}

st.title("Kalkulator Debit Air")
st.markdown("Hitung debit air berdasarkan dua metode: Volume & Waktu atau Luas Penampang & Kecepatan Aliran")

metode = st.radio("Pilih metode perhitungan:", ("Volume & Waktu", "Luas Penampang & Kecepatan"))

if metode == "Volume & Waktu":
    st.subheader("Perhitungan berdasarkan Volume dan Waktu")

    volume = st.number_input("Masukkan volume air:", min_value=0.0, format="%.3f")
    satuan_volume = st.selectbox("Satuan volume:", ["m³", "L"])

    waktu = st.number_input("Masukkan waktu:", min_value=0.1, format="%.2f")
    satuan_waktu = st.selectbox("Satuan waktu:", ["s", "menit", "jam"])

    if st.button("Hitung Debit"):
        hasil = hitung_debit_volume_waktu(volume, waktu, satuan_volume, satuan_waktu)
        st.success(f"Debit air: {hasil['m³/s']:.6f} m³/s")
        st.success(f"Debit air: {hasil['L/s']:.6f} L/s")

elif metode == "Luas Penampang & Kecepatan":
    st.subheader("Perhitungan berdasarkan Luas Penampang dan Kecepatan")

    bentuk = st.selectbox("Pilih bentuk penampang:", ["Lingkaran (Pipa)", "Persegi / Persegi Panjang (Saluran)"])

    if bentuk == "Lingkaran (Pipa)":
        diameter = st.number_input("Masukkan diameter pipa (meter):", min_value=0.01, format="%.3f")
        luas = hitung_luas_penampang_lingkaran(diameter)
        st.info(f"Luas penampang: {luas:.4f} m²")
    else:
        panjang = st.number_input("Lebar saluran (meter):", min_value=0.01, format="%.3f")
        lebar = st.number_input("Kedalaman air (meter):", min_value=0.01, format="%.3f")
        luas = hitung_luas_penampang_persegi(panjang, lebar)
        st.info(f"Luas penampang: {luas:.4f} m²")

    kecepatan = st.number_input("Masukkan kecepatan aliran (m/s):", min_value=0.0, format="%.3f")

    if st.button("Hitung Debit"):
        hasil = hitung_debit_luas_kecepatan(luas, kecepatan)
        st.success(f"Debit air: {hasil['m³/s']:.6f} m³/s")
        st.success(f"Debit air: {hasil['L/s']:.6f} L/s")
