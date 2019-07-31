import winreg
import re

# 注册表操作
class winregeditor:
    dicList = {}

    def orderDict(self, numkey, DisplayName, DisplayIcon,UninstallString,KeyPath,InstallLocation):
        self.dicList[numkey] = {'DisplayName': DisplayName, 'DisplayIcon': DisplayIcon,'UninstallString':UninstallString,'KeyPath':KeyPath,'InstallLocation':InstallLocation}
        exeIcon = re.compile('.*DLL|.*exe',re.I)
        match = exeIcon.match(DisplayIcon)
        if match: #匹配到exe， 可直接打开
            self.dicList[numkey]['exe'] = match.group()
            #去除双引号
            self.dicList[numkey]['exe'] = self.dicList[numkey]['exe'].replace("\"", "")
        else:  # 没有exe，Icon可为ico 文件
            self.dicList[numkey]['icon'] =DisplayIcon
        return self.dicList


    def getwinreg(self):
        software_name = list()
        try:
            # 定义检测位置
            sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
                       r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']
            q=0
            for i in sub_key:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
                h = winreg.QueryInfoKey(key)[0]
                
                for j in range(0, winreg.QueryInfoKey(key)[0] - 1):
                    DisplayName = ''
                    DisplayIcon = ''
                    UninstallString = ''
                    InstallLocation = ''
                    try:
                        key_name = winreg.EnumKey(key, j)
                        key_path = i + '\\' + key_name
                        KeyPath = 'HKEY_LOCAL_MACHINE\\'+key_path
                        each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
                        DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
                        DisplayName = DisplayName.encode('utf-8')
                        try:
                            DisplayIcon, REG_SZ = winreg.QueryValueEx(each_key, "DisplayIcon")
                            DisplayIcon = DisplayIcon.encode('utf-8')
                            UninstallString,REG_SZ = winreg.QueryValueEx(each_key, "UninstallString")
                            UninstallString = UninstallString.encode('utf-8')
                            InstallLocation,REG_SZ = winreg.QueryValueEx(each_key, "InstallLocation")
                            InstallLocation = InstallLocation.encode('utf-8')

                        except WindowsError:
                            pass
                        # 注册表中同时满足DisplayName 和 DisplayIcon
                        if DisplayName and DisplayIcon :
                            software_name.append(str(DisplayName,encoding='utf-8'))
                            result = self.orderDict(str(q+j), str(DisplayName,encoding='utf-8'),str(DisplayIcon,encoding='utf-8'),UninstallString,KeyPath,InstallLocation)  
                    except WindowsError:
                        pass
                #获取到总得数目
                k=q+h
                #将获取到的值重新赋值
                q = h
            
        except  IOError:
            pass
        else:
            # 定义检测位置
            i = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, i, 0, winreg.KEY_ALL_ACCESS)
            for j in range(0, winreg.QueryInfoKey(key)[0] - 1):
                DisplayName = ''
                DisplayIcon = ''
                UninstallString = ''
                InstallLocation = ''
                try:
                    key_name = winreg.EnumKey(key, j)
                    key_path = i + '\\' + key_name
                    KeyPath = 'HKEY_CURRENT_USER\\'+key_path
                    each_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
                    DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
                    DisplayName = DisplayName.encode('utf-8')
                    try:
                        DisplayIcon, REG_SZ = winreg.QueryValueEx(each_key, "DisplayIcon")
                        DisplayIcon = DisplayIcon.encode('utf-8')
                        UninstallString,REG_SZ = winreg.QueryValueEx(each_key, "UninstallString")
                        UninstallString = UninstallString.encode('utf-8')
                        InstallLocation,REG_SZ = winreg.QueryValueEx(each_key, "InstallLocation")
                        InstallLocation = InstallLocation.encode('utf-8')
                    except WindowsError:
                        pass
                    # 注册表中同时满足DisplayName 和 DisplayIcon
                    if DisplayName and DisplayIcon:
                        software_name.append(str(DisplayName,encoding='utf-8'))
                        result = self.orderDict(str(q+j), str(DisplayName,encoding='utf-8'),str(DisplayIcon,encoding='utf-8'),UninstallString,KeyPath,InstallLocation)  
                except WindowsError:
                    pass
        software_name = list(set(software_name))
        software_name = sorted(software_name)
        

        return software_name,result