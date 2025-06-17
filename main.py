from dotenv import load_dotenv
import os

def define_env(env):
    load_dotenv()

    env.variables['COMPANY_NAME'] = os.getenv('COMPANY_NAME', 'Reset')
    env.variables['SUPPORT_EMAIL'] = os.getenv('SUPPORT_EMAIL', 'suporte@reset-bank.com')
    env.variables['COMPLIANCE_EMAIL'] = os.getenv('COMPLIANCE_EMAIL', 'compliance@reset-bank.com')
    env.variables['PAY_API_URL'] = os.getenv('PAY_API_URL', 'https://api.pixease.reset-bank.com/api')

