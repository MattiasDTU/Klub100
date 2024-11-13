# **How to Download FFmpeg** #
credit: https://transloadit.com/devtips/how-to-install-ffmpeg-on-windows-a-complete-guide/
### Step 1. Downloading the .exe file ###
1.1 You will need to go to: https://github.com/BtbN/FFmpeg-Builds/releases

1.2 Download file that fits your computer interface (Win, IOS, Linux)
### Step 2. Extract the FFmpeg archive ###
2.1 Locate the downloaded zip file in your Downloads folder.

2.2 Right-click on the file and select 'Extract All...'.

2.3 Choose a destination folder for extraction. For example, you could create a new folder called 'FFmpeg' in your C: drive.

2.4 Click 'Extract' to unzip the files.
### Step 3: Add FFmpeg to system path ###
3.1 Open the Start menu and search for 'Environment Variables'.

3.2 Click on 'Edit the system environment variables'.

3.3 In the System Properties window, click the 'Environment Variables' button.

3.4 Under 'System variables', find and select the 'Path' variable, then click 'Edit'.

3.5 Click 'New' and add the path to the 'bin' folder inside your FFmpeg extraction directory. For example: 'C:\FFmpeg\bin'

3.6 Click 'OK' to close all windows.
### Step 4: Verify the installation ###
4.1 Open a new Command Prompt window (search for 'cmd' in the Start menu).

4.2 Type ffmpeg -version and press Enter.

4.3 If FFmpeg is properly installed, you should see version information and configuration details.

