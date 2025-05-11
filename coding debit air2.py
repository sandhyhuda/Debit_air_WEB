import streamlit as st
import math

st.set_page_config(page_title="Kalkulator Debit Air", layout="centered")

st.title("💧 Kalkulator Debit Air")
st.write("Alat untuk menghitung debit air berdasarkan dua metode:")

# Pilih metode
metode = st.radio("Pilih metode perhitungan:", 
                  ("Volume dan Waktu", "Luas Penampang dan Kecepatan"))

st.divider()

if metode == "Volume dan Waktu":
    st.subheader("Metode 1: Volume dan Waktu")

    volume = st.number_input("Masukkan Volume Air", min_value=0.0, step=0.01)
    volume_unit = st.selectbox("Satuan Volume", ("m³", "Liter"))

    time = st.number_input("Masukkan Waktu", min_value=0.0, step=0.01)
    time_unit = st.selectbox("Satuan Waktu", ("Detik", "Menit", "Jam"))

    if st.button("Hitung Debit (Q)"):
        # Konversi satuan volume
        if volume_unit == "Liter":
            volume_m3 = volume / 1000
        else:
            volume_m3 = volume

        # Konversi satuan waktu
        if time_unit == "Detik":
            time_s = time
        elif time_unit == "Menit":
            time_s = time * 60
        else:  # Jam
            time_s = time * 3600

        if time_s == 0:
            st.error("Waktu tidak boleh 0.")
        else:
            debit_m3s = volume_m3 / time_s
            debit_ls = debit_m3s * 1000

            st.success("Hasil Perhitungan:")
            st.write(f"**Debit Air:** {debit_m3s:.6f} m³/s")
            st.write(f"**Debit Air:** {debit_ls:.2f} L/s")

            with st.expander("📘 Langkah Perhitungan"):
                st.markdown(f"""
                - Volume: `{volume}` {volume_unit} = `{volume_m3}` m³  
                - Waktu: `{time}` {time_unit} = `{time_s}` detik  
                - Rumus: `Q = V / t`  
                - Q = `{volume_m3} / {time_s}`  
                - Q = `{debit_m3s:.6f}` m³/s = `{debit_ls:.2f}` L/s
                """)

else:
    st.subheader("Metode 2: Luas Penampang dan Kecepatan")

    bentuk = st.selectbox("Pilih Bentuk Penampang", ("Lingkaran (Pipa)", "Persegi Panjang"))

    if bentuk == "Lingkaran (Pipa)":
        diameter = st.number_input("Masukkan Diameter Pipa (m)", min_value=0.0, step=0.001)
        radius = diameter / 2
        luas = math.pi * (radius ** 2)

    else:  # Persegi panjang
        lebar = st.number_input("Masukkan Lebar Saluran (m)", min_value=0.0, step=0.001)
        kedalaman = st.number_input("Masukkan Kedalaman Air (m)", min_value=0.0, step=0.001)
        luas = lebar * kedalaman

    kecepatan = st.number_input("Kecepatan Aliran Air (m/s)", min_value=0.0, step=0.01)

    if st.button("Hitung Debit (Q)"):
        debit_m3s = luas * kecepatan
        debit_ls = debit_m3s * 1000

        st.success("Hasil Perhitungan:")
        st.write(f"**Luas Penampang:** {luas:.6f} m²")
        st.write(f"**Debit Air:** {debit_m3s:.6f} m³/s")
        st.write(f"**Debit Air:** {debit_ls:.2f} L/s")

        with st.expander("📘 Langkah Perhitungan"):
            if bentuk == "Lingkaran (Pipa)":
                st.markdown(f"""
                - Diameter = `{diameter}` m → jari-jari = `{radius:.3f}` m  
                - Luas = π × r² = `{math.pi:.5f} × {radius:.3f}²` = `{luas:.6f}` m²  
                """)
            else:
                st.markdown(f"""
                - Luas = lebar × kedalaman = `{lebar} × {kedalaman}` = `{luas:.6f}` m²  
                """)
            st.markdown(f"""
            - Kecepatan = `{kecepatan}` m/s  
            - Rumus: `Q = A × v`  
            - Q = `{luas:.6f} × {kecepatan}` = `{debit_m3s:.6f}` m³/s = `{debit_ls:.2f}` L/s
            """)

