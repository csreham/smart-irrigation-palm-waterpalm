import streamlit as st
import numpy as np
import pandas as pd
import time
from datetime import datetime
import matplotlib.pyplot as plt
import random

# إعداد صفحة Streamlit
st.set_page_config(
    page_title="نظام الري الذكي - محاكاة كاملة",
    page_icon="🌴",
    layout="wide"
)

# عنوان التطبيق
st.title("🌴 نظام الري الذكي للنخيل - محاكاة كاملة")
st.markdown("---")

# قسم محاكاة المكونات الإلكترونية
st.header("🔌 محاكاة المكونات الإلكترونية")

# عرض المكونات الافتراضية
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🟦 Arduino Uno")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/38/Arduino_Uno_-_R3.jpg", width=100)
    st.metric("الحالة", "🟢 متصل")
    st.metric("السعر الافتراضي", "$8")

with col2:
    st.subheader("💧 مستشعر الرطوبة")
    st.image("https://www.electronicwings.com/storage/PlatformSection/TopicContent/14/description/FC-28_Soil_Moisture_Sensor.png", width=100)
    st.metric("الحالة", "🟢 يعمل")
    st.metric("السعر الافتراضي", "$3")

with col3:
    st.subheader("🌡️ مستشعر DHT22")
    st.image("https://cdn-shop.adafruit.com/970x728/385-02.jpg", width=100)
    st.metric("الحالة", "🟢 يعمل")
    st.metric("السعر الافتراضي", "$6")

with col4:
    st.subheader("🚰 صمام الري")
    st.image("https://www.electronicscomp.com/image/cache/catalog/solenoid-valve-12v-800x800.jpg", width=100)
    st.metric("الحالة", "🟢 جاهز")
    st.metric("السعر الافتراضي", "$12")

# محاكاة دائرة إلكترونية
st.subheader("🔋 محاكاة الدائرة الإلكترونية")

# رسم دائرة إلكترونية مبسطة
circuit_code = """
⚡ الدائرة الإلكترونية الافتراضية:

☀️ لوح شمسي 30W
    ↓
🔋 بطارية 12V/100Ah  
    ↓
🟦 Arduino Uno
    ↙       ↘        ↙       ↘
💧 A0      🧂 A1    🌡️ D4     🚰 D8
رطوبة      ملوحة   حرارة      صمام
"""

st.code(circuit_code, language='text')

# إعدادات النظام الشمسي
st.sidebar.header("⚙️ إعدادات النظام الشمسي")
solar_power = st.sidebar.slider("قوة الألواح الشمسية (واط)", 10, 50, 30)
battery_capacity = st.sidebar.slider("سعة البطارية (Ah)", 50, 200, 100)

class VirtualElectronicComponents:
    def __init__(self):
        self.arduino_connected = True
        self.sensors_calibrated = True
        self.valve_functional = True
        self.solar_panel_output = 0
        self.battery_level = 70  # %
        
    def simulate_arduino_boot(self):
        """محاكاة تشغيل Arduino"""
        boot_sequence = [
            "🔌 توصيل الطاقة...",
            "🟦 تهيئة Arduino...", 
            "📡 تشغيل المستشعرات...",
            "🌐 الاتصال بالشبكة...",
            "✅ Arduino جاهز للعمل!"
        ]
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, step in enumerate(boot_sequence):
            status_text.text(step)
            progress_bar.progress((i + 1) / len(boot_sequence))
            time.sleep(0.5)
        
        st.success("🎉 تم تشغيل النظام الإلكتروني بنجاح!")
        
    def read_virtual_sensors(self):
        """قراءة بيانات واقعية من مستشعرات افتراضية"""
        # محاكاة قراءات واقعية مع تغيرات طفيفة
        base_moisture = 45.0
        base_salinity = 2.5
        base_temp = 25.0
        base_humidity = 60.0
        
        # إضافة تغيرات واقعية
        current_hour = datetime.now().hour
        temp_variation = 10 * np.sin((current_hour - 6) * np.pi / 12)
        
        return {
            'soil_moisture': max(10, min(100, base_moisture + random.uniform(-2, 2))),
            'soil_salinity': max(1.0, min(8.0, base_salinity + random.uniform(-0.1, 0.1))),
            'temperature': max(15, min(45, base_temp + temp_variation + random.uniform(-1, 1))),
            'humidity': max(20, min(95, base_humidity + 20 * np.sin((current_hour - 6) * np.pi / 12) + random.uniform(-3, 3))),
            'soil_ph': 7.2 + random.uniform(-0.1, 0.1),
            'sensor_status': "🟢 ممتاز"
        }
    
    def control_virtual_valve(self, state, duration=0):
        """التحكم في صمام افتراضي"""
        if state:
            valve_actions = [
                f"🔧 إرسال أمر فتح الصمام...",
                f"⚡ تطبيق 12V على pin D8...", 
                f"🚰 فتح صمام الري...",
                f"⏱️ ضبط المدة: {duration} دقيقة...",
                f"💧 بدء تدفق المياه..."
            ]
            
            for action in valve_actions:
                st.write(action)
                time.sleep(0.3)
                
            return True
        else:
            st.write("🔌 إغلاق صمام الري...")
            return True
    
    def simulate_solar_charging(self, hour):
        """محاكاة شحن الطاقة الشمسية"""
        if 6 <= hour <= 18:
            sun_intensity = np.sin((hour - 6) * np.pi / 12)
            self.solar_panel_output = solar_power * sun_intensity
            charge_rate = self.solar_panel_output * 0.1  # 10% كفاءة شحن
            self.battery_level = min(100, self.battery_level + charge_rate)
        else:
            self.solar_panel_output = 0
            
        return self.solar_panel_output, self.battery_level

# فئات المحاكاة الأخرى (PalmTreeSensors, SmartIrrigationAI) تبقى كما هي
class PalmTreeSensors:
    def __init__(self):
        self.virtual_hardware = VirtualElectronicComponents()
        
    def read_sensors(self):
        """استخدام المستشعرات الافتراضية"""
        return self.virtual_hardware.read_virtual_sensors()

class SmartIrrigationAI:
    def __init__(self):
        self.weights = {
            'soil_moisture': -0.6, 'soil_salinity': 0.4, 
            'temperature': 0.3, 'humidity': -0.2
        }
        
    def decide_irrigation(self, sensor_data, battery_level, hour):
        probability = 0.7 if sensor_data['soil_moisture'] < 35 else 0.3
        irrigation_time = 15 if sensor_data['soil_moisture'] < 30 else 8
        
        if probability > 0.6 and battery_level > 20:
            return True, probability, irrigation_time
        else:
            return False, probability, 0

# واجهة التحكم
st.sidebar.header("🎛️ تحكم يدوي")
manual_irrigation = st.sidebar.button("🚿 ري يدوي", type="secondary")
irrigation_duration = st.sidebar.slider("مدة الري (دقائق)", 1, 30, 10)

# تهيئة الأنظمة
if 'virtual_hardware' not in st.session_state:
    st.session_state.virtual_hardware = VirtualElectronicComponents()
    st.session_state.sensors = PalmTreeSensors()
    st.session_state.ai_system = SmartIrrigationAI()
    st.session_state.irrigation_history = []
    st.session_state.sensor_history = []
    st.session_state.last_sensor_data = st.session_state.sensors.read_sensors()

# زر تشغيل النظام الإلكتروني
if st.sidebar.button("🔌 تشغيل النظام الإلكتروني", type="primary"):
    st.session_state.virtual_hardware.simulate_arduino_boot()

# المحاكاة الرئيسية
if st.button("🔄 قراءة المستشعرات الافتراضية", type="primary"):
    current_hour = datetime.now().hour
    
    # محاكاة الطاقة الشمسية
    solar_output, battery_level = st.session_state.virtual_hardware.simulate_solar_charging(current_hour)
    
    # قراءة المستشعرات الافتراضية
    with st.spinner('📡 جاري قراءة البيانات من المستشعرات الافتراضية...'):
        sensor_data = st.session_state.sensors.read_sensors()
        time.sleep(1)  # محاكاة وقت القراءة
    
    st.session_state.last_sensor_data = sensor_data
    st.session_state.sensor_history.append({
        'timestamp': datetime.now(),
        **sensor_data
    })
    
    # قرار الذكاء الاصطناعي
    should_irrigate, confidence, irrigation_time = st.session_state.ai_system.decide_irrigation(
        sensor_data, battery_level, current_hour
    )
    
    # تنفيذ الري
    irrigation_performed = False
    if should_irrigate or manual_irrigation:
        irrigation_duration = irrigation_time if should_irrigate else irrigation_duration
        
        # التحكم في الصمام الافتراضي
        st.info("🔧 التحكم في المكونات الإلكترونية:")
        success = st.session_state.virtual_hardware.control_virtual_valve(True, irrigation_duration)
        
        if success:
            # محاكاة تأثير الري
            st.session_state.last_sensor_data['soil_moisture'] = min(
                100, st.session_state.last_sensor_data['soil_moisture'] + irrigation_duration * 0.8
            )
            
            # تسجيل حدث الري
            st.session_state.irrigation_history.append({
                'timestamp': datetime.now(),
                'duration': irrigation_duration,
                'auto': should_irrigate,
                'confidence': confidence
            })
            
            irrigation_performed = True

# استخدام البيانات الأخيرة
sensor_data = st.session_state.last_sensor_data

# عرض لوحة التحكم
st.header("📊 لوحة تحكم النظام الافتراضي")

# عرض قراءات المستشعرات
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    moisture_color = "🟢" if sensor_data['soil_moisture'] > 40 else "🟡" if sensor_data['soil_moisture'] > 30 else "🔴"
    st.metric(f"{moisture_color} رطوبة التربة", f"{sensor_data['soil_moisture']:.1f}%")

with col2:
    salinity_color = "🟢" if sensor_data['soil_salinity'] < 3 else "🟡" if sensor_data['soil_salinity'] < 5 else "🔴"
    st.metric(f"{salinity_color} ملوحة التربة", f"{sensor_data['soil_salinity']:.1f} dS/m")

with col3:
    st.metric("🌡️ درجة الحرارة", f"{sensor_data['temperature']:.1f}°C")

with col4:
    st.metric("💦 الرطوبة الجوية", f"{sensor_data['humidity']:.1f}%")

with col5:
    battery_color = "🟢" if st.session_state.virtual_hardware.battery_level > 50 else "🟡" if st.session_state.virtual_hardware.battery_level > 20 else "🔴"
    st.metric(f"{battery_color} طاقة البطارية", f"{st.session_state.virtual_hardware.battery_level:.1f}%")

# مؤشر الري
st.subheader("🚦 حالة نظام الري")
if irrigation_performed:
    st.success("🟢 **الري نشط** - الصمام الافتراضي مفتوح")
    st.balloons()
else:
    if sensor_data['soil_moisture'] < 30:
        st.error("🔴 **الري مطلوب** - رطوبة التربة منخفضة")
    elif sensor_data['soil_moisture'] < 40:
        st.warning("🟡 **مراقبة** - رطوبة التربة متوسطة")
    else:
        st.info("🟢 **حالة طبيعية** - لا حاجة للري")

# معلومات الطاقة الشمسية
st.sidebar.header("☀️ إنتاج الطاقة")
st.sidebar.metric("الإنتاج الحالي", f"{st.session_state.virtual_hardware.solar_panel_output:.1f} واط")
st.sidebar.metric("الطاقة المخزنة", f"{st.session_state.virtual_hardware.battery_level:.1f}%")

# قسم المحاكاة الإلكترونية المتقدمة
st.header("🔧 محاكاة متقدمة للمكونات الإلكترونية")

tab1, tab2, tab3 = st.tabs(["📊 إشارات المستشعرات", "🔋 دائرة الطاقة", "📡 اتصالات"])

with tab1:
    st.subheader("📡 إشارات المستشعرات الافتراضية")
    
    # محاكاة إشارات Analog
    st.write("**إشارات الـ Analog من المستشعرات:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        moisture_voltage = (sensor_data['soil_moisture'] / 100) * 5.0
        st.metric("💧 جهد مستشعر الرطوبة", f"{moisture_voltage:.2f}V")
        
    with col2:
        salinity_voltage = (sensor_data['soil_salinity'] / 10) * 5.0
        st.metric("🧂 جهد مستشعر الملوحة", f"{salinity_voltage:.2f}V")
        
    with col3:
        st.metric("🌡️ قراءة DHT22", "🟢 بيانات صحيحة")

with tab2:
    st.subheader("🔋 محاكاة دائرة الطاقة")
    
    st.write("**تدفق الطاقة في النظام:**")
    power_flow = f"""
    ☀️ اللوح الشمسي: {st.session_state.virtual_hardware.solar_panel_output:.1f} واط
        ↓
    🔋 متحكم الشحن: {st.session_state.virtual_hardware.solar_panel_output * 0.9:.1f} واط
        ↓  
    ⚡ البطارية: {st.session_state.virtual_hardware.battery_level:.1f}%
        ↓
    🟦 Arduino: 0.5 واط
        ↓
    💧 المستشعرات: 0.2 واط
    """
    
    st.code(power_flow, language='text')

with tab3:
    st.subheader("📡 محاكاة الاتصالات")
    
    st.write("**اتصالات النظام الافتراضي:**")
    
    comm_status = {
        "Arduino ←→ المستشعرات": "🟢 I2C/Analog",
        "Arduino ←→ الصمام": "🟢 Digital PWM", 
        "النظام ←→ الواجهة": "🟢 WebSocket",
        "التحديث التلقائي": "🟢 كل 5 ثواني"
    }
    
    for device, status in comm_status.items():
        st.write(f"- {device}: {status}")

st.markdown("---")
st.success("🎯 **ملاحظة:** هذا نظام محاكاة كامل لا يحتاج لشراء أي مكونات حقيقية!")

# تذييل الصفحة
st.markdown("---")
st.caption("🌴 نظام الري الذكي - محاكاة إلكترونية كاملة بدون الحاجة لمكونات حقيقية")