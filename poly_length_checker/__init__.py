# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolyLengthChecker
                                 A QGIS plugin
 This plugin checks the poly line check
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-10-18
        copyright            : (C) 2021 by RMIT
        email                : s3923466@student.rmit.edu.au
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PolyLengthChecker class from file PolyLengthChecker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Poly_Length_Checker import PolyLengthChecker
    return PolyLengthChecker(iface)
