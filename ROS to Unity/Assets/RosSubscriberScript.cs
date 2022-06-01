using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosType = RosMessageTypes.UnityRoboticsDemo.MarkersTypeMsg;

public class RosSubscriberScript : MonoBehaviour
{
    public GameObject cube;
    public GameObject sphere;
    public GameObject mesh;

    void Start()
    {
        cube.SetActive(false);
        sphere.SetActive(false);
        mesh.SetActive(false);
        ROSConnection.GetOrCreateInstance().Subscribe<RosType>("markers", DisplayMarker);
    }

    void DisplayMarker(RosType typeMessage)
    {
        if(typeMessage.c == 1)
        {
            cube.SetActive(true);
        }
        if(typeMessage.s == 2)
        {
            sphere.SetActive(true);
        }
        if(typeMessage.m == 10)
        {
            mesh.SetActive(true);
        }
    }
}