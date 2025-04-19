# easy-undervolt

This is a new method to undervolt and/or overclock modern GPUs. I believe it is the easiest and most reliable method now, which allows you to just specify a top frequency and voltage.

Methods to undervolt or overclock the GPU nowadays are needless complicated Youtube tutorials with multiple methods of dragging around a voltage/frequency graph which is prone to error.

## Steps

1. Download GPU Tweak and install and open it. https://www.asus.com/campaign/GPU-Tweak-III/us/index.php#download

2. First we will export the default voltage curve.
   Click on the triangle next to User Mode. Hover over the entry below, and click the export icon.
   ![image](https://github.com/user-attachments/assets/6c447f97-2dd9-4928-a180-d9f739591a03)

4. Select the profile, set the location to your desktop and export it.
   ![image](https://github.com/user-attachments/assets/5909fa41-a4e0-4169-803a-0bf57afe4240)

5. You'll get an XML file like "User Mode.xml" rename this to "default.xml".
6. Download the undervolt program from us, put it in the Desktop. Run it and set the desired max frequency and voltage.
7. Import the new file called new.xml
   
   ![image](https://github.com/user-attachments/assets/5253f350-1d2e-49ba-b2b9-4633932409f8)
9. Select the new profile. Be sure to click apply.
   ![image](https://github.com/user-attachments/assets/41d51e1e-7445-47ee-af95-f9ddc25a1348)
10. (optional) Verify the voltage curve looks ok by clicking on the **VF Tuner** button under the clock area.
11. Close GPU Tweak or else it will randomly switch to OC Mode.

Now every time you want to change the numbers, you can skip to step 6.

## FAQ

### Why not use MSI Afterburner?
Importing of profiles isn't built-in and is very cumbersome. Voltage curve seems to be broken on my GPU.
