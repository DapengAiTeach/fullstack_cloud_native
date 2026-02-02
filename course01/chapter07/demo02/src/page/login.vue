<script setup>
import { ref } from 'vue';

// 登录表单
const form = ref({
  username: '',
  password: ''
});

// 提交登录表单
function submitForm() {
  if (form.value.username && form.value.password) {
    alert(`欢迎，${form.value.username}！`);
  } else {
    alert('请填写用户名和密码。');
  }
}
</script>
<template>
  <div class="login">
    <div class="bg-layer"></div>
    <el-card class="card">
      <div class="brand">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="g" x1="0" x2="1">
              <stop offset="0" stop-color="#7b61ff" />
              <stop offset="1" stop-color="#00e5ff" />
            </linearGradient>
          </defs>
          <rect x="3" y="3" width="18" height="18" rx="4" stroke="url(#g)" stroke-width="1.6"/>
          <path d="M7 15L12 9l5 6" stroke="url(#g)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <h2>系统登录</h2>
      </div>

      <el-form label-width="0px" class="login-form">
        <el-form-item>
          <el-input v-model="form.username" placeholder="用户名" class="input-modern"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input v-model="form.password" type="password" placeholder="密码" class="input-modern"></el-input>
        </el-form-item>
        <el-form-item class="actions">
          <el-button type="primary" class="btn-login" @click="submitForm">登录</el-button>
        </el-form-item>
        <div class="links">
          <a href="#">忘记密码？</a>
          <a href="#">帮助中心</a>
        </div>
      </el-form>
    </el-card>
  </div>
</template>

<style scoped>
:root{
  --bg-1: #020617;
  --bg-2: #081228;
  --accent-a: #7b61ff;
  --accent-b: #00e5ff;
  --glass: rgba(255,255,255,0.04);
  --glass-border: rgba(120,120,255,0.18);
}
.login{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  position:relative;
  overflow:hidden;
  background: radial-gradient( circle at 10% 10%, rgba(123,97,255,0.08), transparent 10%),
              radial-gradient( circle at 90% 90%, rgba(0,229,255,0.06), transparent 12%),
              linear-gradient(180deg,var(--bg-1),var(--bg-2));
}
.bg-layer{
  position:absolute;inset:0;z-index:0;
  background-image:linear-gradient(135deg, rgba(255,255,255,0.03) 1px, transparent 1px),
                   linear-gradient(225deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size:60px 60px, 140px 140px;
  opacity:0.9;
  animation: drift 18s linear infinite;
}
.card{
  position:relative;z-index:2;
  width:420px;
  padding:32px 32px 24px 32px;
  border-radius:20px;
  background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
  box-shadow: 0 20px 60px rgba(0,0,0,0.3), 
              inset 0 1px 0 rgba(255,255,255,0.3),
              0 0 30px rgba(0,229,255,0.1);
  border: 1.5px solid rgba(255,255,255,0.18);
  backdrop-filter: blur(16px) saturate(180%);
}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:18px}
.brand h2{margin:0;color:#1a3a52;font-size:22px;font-weight:700;letter-spacing:0.8px}

.login-form{color:#f5fbff}
.input-modern .el-input__inner{
  background: rgba(255,255,255,0.08);
  border:1px solid rgba(255,255,255,0.2);
  color: #ffffff;
  padding:12px 14px;
  border-radius:10px;
  font-size:15px;
  transition: all .2s ease;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}
.input-modern .el-input__inner::placeholder{color:rgba(50,100,150,0.7)}
.input-modern .el-input__inner:focus{
  outline:none;
  border-color: rgba(0,229,255,0.8);
  background: rgba(255,255,255,0.12);
  box-shadow:0 0 20px rgba(0,229,255,0.25), inset 0 2px 4px rgba(0,0,0,0.1);
  transform:translateY(-1px);
}
.actions{display:flex;justify-content:flex-end;margin-top:6px}
.btn-login{
  background: linear-gradient(135deg, #5d4dff 0%, #0099dd 100%) !important;
  color:#ffffff !important;
  border:none !important;
  padding:11px 22px;
  border-radius:8px;
  font-weight:800 !important;
  font-size:16px !important;
  box-shadow: 0 8px 28px rgba(93,77,255,0.3);
}
.btn-login:hover{
  transform:translateY(-3px);
  background: linear-gradient(135deg, #6d5dff 0%, #00aaee) !important;
  box-shadow: 0 12px 36px rgba(93,77,255,0.4) !important;
}
:deep(.btn-login span){
  color: #ffffff !important;
  font-weight: 800 !important;
}
.links{display:flex;justify-content:space-between;margin-top:14px;font-size:13px;color:#4a6fa5}
.links a{color:inherit;text-decoration:none}
.links a:hover{color:var(--accent-b);text-decoration:underline}

@keyframes drift{
  0%{transform:translateY(0) rotate(0deg);opacity:0.9}
  50%{transform:translateY(-30px) rotate(3deg);opacity:1}
  100%{transform:translateY(0) rotate(0deg);opacity:0.9}
}
</style>