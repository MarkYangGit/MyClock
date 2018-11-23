using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Timers;
using System.Media;

namespace ClockAI
{


    public partial class ClockAI : Form
    {
        public string time_H;
        public string time_M;


        public bool timeForGetUp = false;


        public ClockAI()
        {
            InitializeComponent();
        }

        private void ClockAI_Load(object sender, EventArgs e)
        {
            //for (int l = 0; l < 24; l++)
            //{
            //    comboBox1.Items.Remove(l.ToString());
            //}
            timer1.Enabled = true;
            TraTimeToComboBox();
        }

        // 遍历一下下拉框里的时间
        private void TraTimeToComboBox()
        {
            //将 0--23 时 添加进入下拉框
            for (int i = 0; i < 24; i++)
            {
                comboBox1.Items.Add(i.ToString());

            }
            //显示现在的 小时 在下拉框
            comboBox1.Text = DateTime.Now.Hour.ToString();

            //将 0--59 分 添加进入下拉框
            for (int l = 0; l < 60; l++)
            {
                comboBox2.Items.Add(l.ToString());
            }
            //显示现在的 分钟 在下拉框
            comboBox2.Text = DateTime.Now.Minute.ToString();


        }



        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            time_H = comboBox1.Text;
            time_M = comboBox2.Text;

            

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //当前时间显示
            label_huor.Text = DateTime.Now.Hour.ToString();
            label_minute.Text = DateTime.Now.Minute.ToString();
            label_second.Text = DateTime.Now.Second.ToString();

            string Hour = DateTime.Now.Hour.ToString();
            string Minuste = DateTime.Now.Minute.ToString();
            if (Hour == time_H && Minuste == time_M && DateTime.Now.Second.ToString() == "0")
            {


                //string path = "F:/Project/MySelfPrpject/PythonToGet/" + "Weathers_" + DateTime.Now.ToString("yyyy-MM-dd") + "/weather_" +
                //    DateTime.Now.ToString("yyyy-MM-dd") + ".wav";   //.ToString();//.wav音频文件路径

                //SoundPlayer player = new SoundPlayer(@path);
                //player.Play();//简单播放一遍
                //player.PlayLooping();//循环播放
                //player.PlaySync();//另起线程播放

                PlayWeather();
                PlayNews();



                //timeForGetUp = true;
                //MessageBox.Show("时间到！", "警告", MessageBoxButtons.OK);

            }

            void PlayWeather()
            {
                MP3Player.MP3Player mP3 = new MP3Player.MP3Player();

                mP3.FilePath = "F:/Project/MySelfPrpject/PythonToGet/" + "Weathers_" + DateTime.Now.ToString("yyyy-MM-dd") + "/weather_" +
                    DateTime.Now.ToString("yyyy-MM-dd") + ".mp3";
                mP3.Play();
            }

            void PlayNews()
            {
                for (int i = 0; i < 9; i++)
                {

                    MP3Player.MP3Player mP3 = new MP3Player.MP3Player();

                    mP3.FilePath = "F:/Project/MySelfPrpject/PythonToGet/" + "News_" + DateTime.Now.ToString("yyyy-MM-dd") + "/News_" + i.ToString()
               + "_" + DateTime.Now.ToString("yyyy-MM-dd") + ".mp3";
                    mP3.Play();

                }
            }

        }
    }
}
